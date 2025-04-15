from PriceScraper import PriceScraper
from EmailSender import EmailSender
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
price_scraper = PriceScraper(url)
price =  price_scraper.price
below = 100
if price< below:
    email_sender = EmailSender(below, price, url)
    email_sender.send_email()

