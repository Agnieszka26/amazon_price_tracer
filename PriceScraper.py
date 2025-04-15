from bs4 import BeautifulSoup
import requests


class PriceScraper:
    def __init__(self, url):
        website = requests.get(url)
        website.raise_for_status()
        w = website.text
        sp = BeautifulSoup(w, "html.parser")
        price_whole = sp.select_one(".a-price-whole").getText()
        price_fraction = sp.select_one(".a-price-fraction").getText()
        price = f"{price_whole}{price_fraction}"
        self.price = float(price)




