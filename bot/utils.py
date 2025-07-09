import logging

def setup_logger():
    logging.basicConfig(
        filename='logs/bot.log',
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def validate_order_input(order_type, side, symbol, quantity, price=None):
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Invalid order type")
    if side not in ['BUY', 'SELL']:
        raise ValueError("Invalid order side")
    if not isinstance(quantity, (int, float)):
        raise ValueError("Quantity must be a number")
    if order_type == 'LIMIT' and price is None:
        raise ValueError("Price required for limit order")
