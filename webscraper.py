import requests
from bs4 import BeautifulSoup
class WebScraper:
    def __init__(self, url) -> None:
        self.url = url

    def get_world_list_rows(self):
        response = requests.get(self.url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        tbody = table.find('tbody')
        return tbody.find_all('tr')

        
