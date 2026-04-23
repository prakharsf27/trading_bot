from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_symbol, validate_side, validate_order_type, 
    validate_quantity, validate_price
)
from bot.logging_config import setup_logging

logger = setup_logging()

class OrderManager:
    def __init__(self, api_key, api_secret):
        self.client = BinanceFuturesClient(api_key, api_secret)

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """
        Validates input and places the order.
        """
        try:
            # Validation
            symbol = validate_symbol(symbol)
            side = validate_side(side)
            order_type = validate_order_type(order_type)
            quantity = validate_quantity(quantity)
            price = validate_price(price) if price else None
            stop_price = validate_price(stop_price) if stop_price else None

            logger.info(f"Processing {order_type} order for {symbol}")

            if order_type == "MARKET":
                return self.client.place_futures_order(symbol, side, "MARKET", quantity)
            elif order_type == "LIMIT":
                return self.client.place_futures_order(symbol, side, "LIMIT", quantity, price)
            elif order_type == "STOP_LIMIT":
                if not stop_price:
                    raise ValueError("Stop Price is required for STOP_LIMIT orders.")
                return self.client.place_stop_limit_order(symbol, side, quantity, price, stop_price)
            
        except Exception as e:
            logger.error(f"Order placement failed: {e}")
            raise
