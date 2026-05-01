import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

def prompt_if_missing(value, text):
    return value if value else input(text).strip()

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity")
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        print("\n=== Trading Bot ===")

        symbol = prompt_if_missing(args.symbol, "Enter Symbol (e.g. BTCUSDT): ").upper()
        side = validate_side(
            prompt_if_missing(args.side, "Enter Side (BUY/SELL): ")
        )

        order_type = validate_order_type(
            prompt_if_missing(args.type, "Enter Order Type (MARKET/LIMIT): ")
        )

        quantity = validate_quantity(
            prompt_if_missing(args.quantity, "Enter Quantity: ")
        )

        price = None

        if order_type == "LIMIT":
            price = validate_price(
                prompt_if_missing(args.price, "Enter Limit Price: ")
            )

        print("\nOrder Request Summary")
        print("----------------------")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        if price:
            print("Price:", price)

        client = get_client()

        result = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\nOrder Response")
        print("----------------------")
        print("Order ID:", result["orderId"])
        print("Status:", result["status"])
        print("Executed Qty:", result["executedQty"])
        print("Avg Price:", result.get("avgPrice", "N/A"))

        print("\nSUCCESS")

    except Exception as e:
        print("\nFAILED:", e)

if __name__ == "__main__":
    main()