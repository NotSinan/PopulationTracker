from webscraper import WebScraper
from worldlistprocessor import WorldListProcessor
import time
import argparse
from prettyprinter import PrettyPrinter
import pyfiglet
import msvcrt

def main(threshold):
    print(pyfiglet.figlet_format("OSRS Population Tracker"))
    web_scraper = WebScraper("https://oldschool.runescape.com/slu?order=WMLPA")
    world_list_processor = WorldListProcessor(threshold)
    pretty_print = PrettyPrinter()

    while True:
        rows = web_scraper.get_world_list_rows()
        pretty_print.prettyprint(world_list_processor.get_population(rows))
        
        # Check for user input to exit the program
        if msvcrt.kbhit():
            key = msvcrt.getch().decode()
            if key.lower() == "q":
                print("Exiting the program...")
                break

        time.sleep(10)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="oldschool runescape population tracker")
    parser.add_argument('-t', '--threshold', type=int, default=5, help='threshold for population difference')
    args = parser.parse_args()
    main(args.threshold)
