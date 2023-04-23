# Exchange Rate Email Sender

This Python script sends an email containing the daily Euro and Dollar exchange rates with Turkish Lira to a list of email addresses. The email is sent every day at 9 am and the exchange rates are scraped from the x-rates.com website.

## Prerequisites
- Python 3.6 or higher.
- Requests, Beautiful Soup 4, dotenv and Flask Python modules.

## Getting Started

1. Clone this repository or download the `exchange_rate_email_sender.py` file.
2. Install the required Python modules using pip: `pip install requests beautifulsoup4 dotenv Flask`.
3. Set up a Gmail account to send the emails from.
4. Create a `.env` file in the same directory as the `exchange_rate_email_sender.py` file with the following information:
   - `SENDER_EMAIL`: the email address of the Gmail account you will use to send the emails.
   - `RECEIVER_EMAILS`: a comma-separated list of email addresses to send the emails to.
   - `EMAIL_PASSWORD`: the password for the Gmail account you will use to send the emails.
5. Run the script by running the `exchange_rates_sender.py` file.

## How it works

The script uses the following steps to send the email with exchange rates:

1. It imports the necessary Python modules and loads the environment variables from the `.env` file.
2. It sets up the URL to get the exchange rates from and the currency pairs to get exchange rates for.
3. It defines a function to scrape the exchange rates from the website and a function to send an email with the exchange rates.
4. It initializes a Flask application and defines a route for the main functionality.
5. When the script is run, the Flask application is started and the route is accessed.
6. The script gets the exchange rates and measures the time taken.
7. The script sends the email with the exchange rates and measures the time taken.
8. The script prints a success message and returns a response. 
