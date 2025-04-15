import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

GMAIL_ADDRESS= os.getenv('GMAIL_ADDRESS')
GMAIL_PASSWORD= os.getenv('GMAIL_PASSWORD')
GMAIL_HOST_NAME=os.getenv("GMAIL_HOST_NAME")
PORT = int(os.getenv('PORT'))
TIMEOUT = int(os.getenv('TIMEOUT'))

class EmailSender:
    def __init__(self, below, price, url):
        self.msg = (f"Subject: Amazon Price Alert \n\n Hello! Your desired item is below ${below}, now it is ${price}. "
                    f"Check it out on {url}!")
    def send_email(self):
        with smtplib.SMTP(GMAIL_HOST_NAME, PORT, timeout=TIMEOUT) as connection:
            connection.starttls()
            connection.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
            connection.sendmail(from_addr=GMAIL_ADDRESS, to_addrs="agna.medrek@gmail.com", msg =self.msg)
        print(f"Email: {self.msg} was send")
