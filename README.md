# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot built for the Primetrade.ai Python Developer Application Task.  
This bot connects to Binance Futures Testnet and allows users to place MARKET and LIMIT orders with proper validation, logging, and clean modular code structure.

---

## Features

✅ Place MARKET Orders  
✅ Place LIMIT Orders  
✅ BUY / SELL Support  
✅ Binance Futures Testnet Integration  
✅ Interactive CLI Input Mode  
✅ Argument-based CLI Mode  
✅ Input Validation  
✅ Error Handling  
✅ Request / Response Logging  
✅ Clean Modular Structure

---

## Tech Stack

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging

---

## Project Structure

```text
trading_bot/
│── bot/
│   │── __init__.py
│   │── client.py
│   │── orders.py
│   │── validators.py
│   │── logging_config.py
│
│── logs/
│   │── trading.log
│
│── cli.py
│── requirements.txt
│── .gitignore
│── README.md
│── .env   (local only, not uploaded)
```

## Installation

pip install -r requirements.txt

## Environment Setup

Create `.env`

```
BINANCE_API_KEY=lbcrvEIfCDdmFv9FqA4p9BXIlPqaEhC4mgCZ6X0Nrb0zYCOGhvHsDxyeowm40v0A
BINANCE_API_SECRET=cJMnU6GerS85aWpXOn2VJ4LlyKkSLbvGxUv1ICb82N36d1MyA9phQ60wN9pfKMxf
```

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
