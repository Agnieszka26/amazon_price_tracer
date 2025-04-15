from PriceScraper import PriceScraper
from EmailSender import EmailSender
url = "https://appbrewery.github.io/instant_pot/"
price_scraper = PriceScraper(url)
price =  price_scraper.price
below = 100
if price< below:
    email_sender = EmailSender(below, price, url)
    email_sender.send_email()

