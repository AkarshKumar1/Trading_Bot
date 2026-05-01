import os
from dotenv import load_dotenv

try:
    from binance.client import Client
except ImportError:
    from binance import Client

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("Missing BINANCE_API_KEY or BINANCE_API_SECRET in .env file")

    return Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )