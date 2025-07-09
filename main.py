from bot.basic_bot import BasicBot
from bot.order_manager import OrderManager
from bot.utils import setup_logger, validate_order_input

def main():
    setup_logger()
    bot = BasicBot()
    order_mgr = OrderManager(bot.client)

    print("Welcome to the Binance Futures Testnet Trading Bot")
    order_type = input("Enter order type (MARKET / LIMIT): ").upper()
    side = input("Enter side (BUY / SELL): ").upper()
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None

    if order_type == 'LIMIT':
        price = input("Enter price: ")

    try:
        validate_order_input(order_type, side, symbol, quantity, price)
        if order_type == 'MARKET':
            result = order_mgr.place_market_order(symbol, side, quantity)
        else:
            result = order_mgr.place_limit_order(symbol, side, quantity, price)

        print("Order Result:", result)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
