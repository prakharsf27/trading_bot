import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logging

logger = setup_logging()

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        """
        Initializes the Binance Futures Testnet client.
        """
        try:
            # We use the testnet=True flag and manually specify the base URL for futures testnet
            self.client = Client(api_key, api_secret, testnet=True)
            # Binance Futures Testnet Base URL: https://testnet.binancefuture.com
            # The python-binance client handles the URL logic when testnet=True is passed, 
            # but we can also set the futures base URL explicitly if needed.
            logger.info("Binance Futures Testnet client initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize Binance client: {e}")
            raise

    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        """
        Places a futures order (MARKET or LIMIT).
        """
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
            }

            if order_type.upper() == "LIMIT":
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params["price"] = price
                params["timeInForce"] = "GTC"  # Good Till Cancelled is standard for Limit orders

            logger.info(f"Sending order request: {params}")
            
            # Use futures_create_order for USDT-M Futures
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order response received: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while placing order: {e}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """
        Places a STOP_LIMIT order (Bonus feature).
        """
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": "STOP",
                "quantity": quantity,
                "price": price,
                "stopPrice": stop_price,
                "timeInForce": "GTC"
            }
            logger.info(f"Sending Stop-Limit order request: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"Stop-Limit response received: {response}")
            return response
        except Exception as e:
            logger.error(f"Failed to place Stop-Limit order: {e}")
            raise
