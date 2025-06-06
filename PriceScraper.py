from bs4 import BeautifulSoup
import requests
headers={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "pl-PL,pl;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
"Priority": "u=0, i",
"Sec-Ch-Ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": "\"Windows\"",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",

}

class PriceScraper:
    def __init__(self, url):
        website = requests.get(url, headers=headers)
        website.raise_for_status()
        w = website.text
        sp = BeautifulSoup(w, "html.parser")
        price_whole = sp.select_one(".a-price-whole").getText()
        price_fraction = sp.select_one(".a-price-fraction").getText()
        price = f"{price_whole}{price_fraction}"
        self.price = float(price)




