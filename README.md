# Binance Futures Testnet Trading Bot

A Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- MARKET orders
- LIMIT orders
- BUY / SELL support
- Input validation
- Logging
- Error handling
- Modular code structure

## Project Structure

trading_bot/
│── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│── cli.py
│── requirements.txt

## Installation

pip install -r requirements.txt

## Environment Setup

Create `.env`

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

## Run Bot

python cli.py

## Example Inputs

BTCUSDT
BUY
MARKET
0.001

## Logs

Saved inside logs/trading.log

## Author

Akarsh Kumar