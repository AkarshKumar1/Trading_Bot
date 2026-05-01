# Binance Futures Testnet Trading Bot

A simplified Python trading bot built for the **Primetrade.ai Python Developer Hiring Task**.  
This application connects to **Binance Futures Testnet (USDT-M)** and allows users to place **MARKET** and **LIMIT** orders through a clean Command Line Interface (CLI).

The project focuses on clean architecture, reusable code, logging, input validation, and exception handling.

---

## Objective

Build a Python application that can:

- Place **Market Orders**
- Place **Limit Orders**
- Support **BUY** and **SELL**
- Accept user input through CLI
- Validate inputs
- Log requests / responses / errors
- Handle API and network exceptions
- Maintain clean project structure

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
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── trading.log
├── cli.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env   (local only, not uploaded)
```

## Features

- Binance Futures Testnet Integration
- MARKET Orders
- LIMIT Orders
- BUY / SELL Support
- Interactive CLI Mode
- Argument-based CLI Mode
- Input Validation
- Error Handling
- Structured Logging
- Modular Codebase

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/AkarshKumar1/Trading_Bot.git
cd binance_trading_bot
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Binance Futures Testnet Account

Use:

https://testnet.binancefuture.com

Generate:

- API Key
- Secret Key

### 4. Create `.env` File

Create a file named `.env` in the root folder:

```env
BINANCE_API_KEY=lbcrvEIfCDdmFv9FqA4p9BXIlPqaEhC4mgCZ6X0Nrb0zYCOGhvHsDxyeowm40v0A
BINANCE_API_SECRET=cJMnU6GerS85aWpXOn2VJ4LlyKkSLbvGxUv1ICb82N36d1MyA9phQ60wN9pfKMxf
```

## How to Run

### Option 1: Interactive CLI Mode

```bash
python cli.py
```
Then enter:
```
Enter Symbol (e.g. BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Order Type (MARKET/LIMIT): MARKET
Enter Quantity: 0.001
```

### Option 2: CLI Arguments Mode 

MARKET Order Example
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```
LIMIT Order Example
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Sample Output

```
=== Trading Bot ===

Order Request Summary
----------------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Response
----------------------
Order ID: 13096555722
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00

SUCCESS
```

## Logging

All requests, responses, and errors are stored in:

```text
logs/trading.log
```

### Example: 
```text
2026-05-01 19:05:21 - INFO - Request: BTCUSDT BUY MARKET qty=0.001
2026-05-01 19:05:23 - INFO - Response: OrderId=13096555722 Status=NEW
```
## Input Validation

The bot validates:

- Symbol is required
- Side must be BUY or SELL
- Order type must be MARKET or LIMIT
- Quantity must be positive
- Price is required for LIMIT orders

## Error Handling

Handles:

- Invalid inputs
- Missing API credentials
- Binance API errors
- Network failures
- Unexpected exceptions

## Assumptions

- Binance Futures Testnet account is active
- Valid API credentials are configured
- Internet connection available
- Testnet responses may differ from live exchange

## Deliverables Covered

- Source Code
- README.md
- requirements.txt
- Logging Files
- MARKET Order Support
- LIMIT Order Support
- BUY / SELL Support
- Validation
- Error Handling
- Clean Structure

## Author

Akarsh Kumar

# Submission Note

This project was developed as part of the Primetrade.ai Python Developer Hiring Round Task.
