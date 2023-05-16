from webscraper import WebScraper
from worldlistprocessor import WorldListProcessor
import time
import argparse
from prettyprinter import PrettyPrinter
import pyfiglet
from halo import Halo

def main(threshold):
    try:
        print(pyfiglet.figlet_format("OSRS Population Tracker"))
        web_scraper = WebScraper("https://oldschool.runescape.com/slu?order=WMLPA")
        world_list_processor = WorldListProcessor(threshold)
        pretty_print = PrettyPrinter()
        spinner = Halo(text='Loading...', spinner='dots10', text_color="red", animation='marquee', color='red')

        while True:
            rows = web_scraper.get_world_list_rows()
            pretty_print.prettyprint(world_list_processor.get_population(rows))
            spinner.text_color = "red"
            with spinner.start():
                time.sleep(10)
                spinner.text_color = "green"
                spinner.succeed("OK")
    
    except KeyboardInterrupt:
        print("You have now exited the application.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="oldschool runescape population tracker")
    parser.add_argument('-t', '--threshold', type=int, default=5, help='threshold for population difference')
    args = parser.parse_args()
    main(args.threshold)
