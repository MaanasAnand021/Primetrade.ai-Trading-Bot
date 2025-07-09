import logging

class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing limit order: {e}")
            return None
