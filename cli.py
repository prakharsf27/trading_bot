import click
import os
from dotenv import load_dotenv
from bot.orders import OrderManager
from tabulate import tabulate
import logging

# Load environment variables from .env if it exists
load_dotenv()

@click.group()
def main():
    """
    Binance Futures Trading Bot CLI
    """
    pass

@main.command()
@click.option('--symbol', required=True, help='Trading symbol (e.g., BTCUSDT)')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side')
@click.option('--type', 'order_type', required=True, type=click.Choice(['MARKET', 'LIMIT', 'STOP_LIMIT'], case_sensitive=False), help='Order type')
@click.option('--quantity', required=True, type=float, help='Order quantity')
@click.option('--price', type=float, help='Limit price (required for LIMIT/STOP_LIMIT)')
@click.option('--stop-price', type=float, help='Stop price (required for STOP_LIMIT)')
@click.option('--api-key', envvar='BINANCE_API_KEY', help='Binance API Key')
@click.option('--api-secret', envvar='BINANCE_API_SECRET', help='Binance API Secret')
def order(symbol, side, order_type, quantity, price, stop_price, api_key, api_secret):
    """
    Place a futures order.
    """
    if not api_key or not api_secret:
        click.secho("Error: API Key and Secret are required (via options or .env)", fg='red')
        return

    try:
        manager = OrderManager(api_key, api_secret)
        response = manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        # Success Output
        click.secho("\n✅ Order Placed Successfully!", fg='green', bold=True)
        
        # Format response for display
        table_data = [
            ["OrderID", response.get('orderId')],
            ["Symbol", response.get('symbol')],
            ["Status", response.get('status')],
            ["Executed Qty", response.get('executedQty')],
            ["Avg Price", response.get('avgPrice', 'N/A')],
            ["Type", response.get('type')],
            ["Side", response.get('side')]
        ]
        
        click.echo(tabulate(table_data, tablefmt="fancy_grid"))

    except Exception as e:
        click.secho(f"\n❌ Error: {str(e)}", fg='red', bold=True)

if __name__ == "__main__":
    main()
