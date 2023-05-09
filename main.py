from webscraper import WebScraper
from worldlistprocessor import WorldListProcessor
import time
if __name__ == "__main__":
    print("Application started")
    scraper = WebScraper("https://oldschool.runescape.com/slu?order=WMLPA")
    wlp = WorldListProcessor()

    while True:
        rows = scraper.get_world_list_rows()
        wlp.get_population(rows)
        time.sleep(10)
    
