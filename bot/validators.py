import re

def validate_symbol(symbol):
    if not re.match(r"^[A-Z0-9]{5,15}$", symbol.upper()):
        raise ValueError(f"Invalid symbol: {symbol}. Must be alphanumeric (e.g., BTCUSDT).")
    return symbol.upper()

def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
    return side.upper()

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError(f"Invalid order type: {order_type}. Supported: MARKET, LIMIT, STOP_LIMIT.")
    return order_type.upper()

def validate_quantity(quantity):
    try:
        q = float(quantity)
        if q <= 0:
            raise ValueError
        return q
    except ValueError:
        raise ValueError(f"Invalid quantity: {quantity}. Must be a positive number.")

def validate_price(price):
    if price is None:
        return None
    try:
        p = float(price)
        if p <= 0:
            raise ValueError
        return p
    except ValueError:
        raise ValueError(f"Invalid price: {price}. Must be a positive number.")
