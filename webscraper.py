import requests
from bs4 import BeautifulSoup
class WebScraper:
    def __init__(self, url) -> None:
        self.url = url
        self.response = requests.get(self.url)
        self.html = self.response.content
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_world_list_rows(self):
        table = self.soup.find('table')
        tbody = table.find('tbody')
        return tbody.find_all('tr')

        
