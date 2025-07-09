from binance.client import Client
from config.config import API_KEY, API_SECRET, BASE_URL

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL
        self.client.API_URL = BASE_URL  # Override base URL for testnet

    def get_balance(self):
        return self.client.futures_account_balance()
