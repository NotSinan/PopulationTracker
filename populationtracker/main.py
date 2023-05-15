from populationtracker.webscraper import WebScraper
from populationtracker.worldlistprocessor import WorldListProcessor
import time
import argparse

def main(threshold):
    print("Application started")
    scraper = WebScraper("https://oldschool.runescape.com/slu?order=WMLPA")
    wlp = WorldListProcessor(threshold)

    while True:
        rows = scraper.get_world_list_rows()
        wlp.get_population(rows)
        time.sleep(10)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OldSchool RuneScape Population Tracker.")
    parser.add_argument('-t', '--threshold', type=int, default=5, help='Threshold for population difference')
    args = parser.parse_args()
    main(args.threshold)
