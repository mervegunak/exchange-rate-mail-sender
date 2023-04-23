from email.mime.text import MIMEText
from typing import List, Tuple
import os
import smtplib
import ssl
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from flask import Flask

# Load environment variables from .env file
load_dotenv()

# Get email-related environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAILS_STR = os.getenv("RECEIVER_EMAILS")
RECEIVER_EMAILS: List[str] = RECEIVER_EMAILS_STR.split(',')
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Set up URL and currency pairs to get exchange rates for
URL = "https://www.x-rates.com/calculator/?from={}&to={}"
CURRENCIES: List[Tuple[str, str]] = [("USD", "TRY"), ("EUR", "TRY")]

# Define function to get exchange rates from website
def get_exchange_rates() -> Tuple[str, str]:
    rates = {}
    for currency in CURRENCIES:
        response = requests.get(URL.format(currency[0], currency[1]))
        soup = BeautifulSoup(response.text, "html.parser")
        exchange_rate = soup.find('span', {'class': 'ccOutputRslt'}).text
        rates[currency] = exchange_rate
    return rates[CURRENCIES[0]], rates[CURRENCIES[1]]

# Define function to send email with exchange rates
def send_email(dolar_rate: str, euro_rate: str):
    # Format HTML message with exchange rates
    html = f"""\
    <html>
    <body>
        <p>Today's exchange rates are:</p>
        <ul>
        <li>Dolar/TL: {dolar_rate}</li>
        <li>Euro/TL: {euro_rate}</li>
        </ul>
    </body>
    </html>
    """

    # Create message object with MIMEText
    message = MIMEText(html, "html")
    message["Subject"] = "Exchange Rates Update"
    message["From"] = "Daily Exchange Rates"
    message["To"] = ", ".join(RECEIVER_EMAILS)

    # Set up SMTP server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, message.as_string())

# Initialize Flask application
app = Flask(__name__)

# Define Flask route
@app.route('/')
def main():
    try:
        # Get exchange rates and measure time taken
        print("Getting exchange rates...")
        start_time = time.time()
        dolar_rate, euro_rate = get_exchange_rates()
        end_time = time.time()
        print(f"Dolar rate: {dolar_rate}")
        print(f"Euro rate: {euro_rate}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")

        # Send email with exchange rates and measure time taken
        print("Sending email...")
        start_time = time.time()
        send_email(dolar_rate, euro_rate)
        end_time = time.time()

        # Print success message and return response
        print(f"Email sent! Time taken: {end_time - start_time:.2f} seconds")
        return "Email sent!"
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run()
