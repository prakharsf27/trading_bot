# Binance Futures Trading Bot (Simplified)

A lightweight Python-based trading bot for placing orders on the **Binance Futures Testnet (USDT-M)**.

## Features
- **Order Types**: Supports `MARKET`, `LIMIT`, and `STOP_LIMIT` (Bonus).
- **Sides**: Supports `BUY` and `SELL`.
- **Validation**: Strict input validation for symbols, quantities, and prices.
- **Logging**: Detailed logging of all API requests and responses to `bot.log`.
- **CLI UX**: Clean command-line interface using `Click` and tabular output.
- **Error Handling**: Comprehensive handling of API errors and network issues.

## Project Structure
```text
binance_trading_bot/
  bot/
    client.py        # Binance API wrapper (USDT-M Futures)
    orders.py        # Orchestration and business logic
    validators.py    # Input validation logic
    logging_config.py# Logger setup
  cli.py             # CLI Entry point
  README.md
  requirements.txt
  .env               # API Keys (optional)
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Binance Futures Testnet API Key and Secret. Register at [testnet.binancefuture.com](https://testnet.binancefuture.com/).

### 2. Installation
```bash
# Clone or navigate to the directory
cd binance_trading_bot

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables (Optional)
Create a `.env` file in the root directory to store your keys securely:
```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

## Usage Examples

### Place a Market Order
```bash
python cli.py order --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order
```bash
python cli.py order --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

### Place a Stop-Limit Order (Bonus)
```bash
python cli.py order --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 65000 --stop-price 64500
```

## Logging
Logs are saved to `bot.log` in the root directory. It contains:
- Request parameters sent to Binance.
- Raw API response details.
- Error tracebacks and validation failures.

## Assumptions
- The bot targets the **USDT-M Futures Testnet** exclusively.
- `TimeInForce` for Limit orders is defaulted to `GTC` (Good Till Cancelled).
- Precision requirements for different symbols are assumed to be handled by the user (inputting valid decimal places).
