import requests
from bs4 import BeautifulSoup
import time

class WebScrapper:
    def __init__(self, website: str, freq: int):
        self._website = website
        self._freq = freq
        self._parsers = []
        self._soup: BeautifulSoup = None
        self.get_soup()

    def get_soup(self):
        r = requests.get(self._website)
        soup = BeautifulSoup(r.text, 'html.parser')
        self._soup = soup

    def avaiable(self):
        try:
            text = self._soup.find(id="cont_form").h1.center.text.strip()
            str = 'En este momento la parroquia no cuenta con cupos para enfermos'
            if str in text:
                avaiable = False
            else:
                avaiable = True
        except:
            avaiable = False
            text = 'No se encontro el texto'
        return avaiable, text    
    