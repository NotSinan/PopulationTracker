from webscraper import WebScraper
from worldlistprocessor import WorldListProcessor
import time
import argparse
from prettyprinter import PrettyPrinter
import pyfiglet

def main(threshold):
    print(pyfiglet.figlet_format("OSRS Population Tracker"))
    scraper = WebScraper("https://oldschool.runescape.com/slu?order=WMLPA")
    wlp = WorldListProcessor(threshold)
    pretty_print = PrettyPrinter()

    while True:
        rows = scraper.get_world_list_rows()
        pretty_print.prettyprint(wlp.get_population(rows))
        time.sleep(10)
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OldSchool RuneScape Population Tracker.")
    parser.add_argument('-t', '--threshold', type=int, default=5, help='Threshold for population difference')
    args = parser.parse_args()
    main(args.threshold)
