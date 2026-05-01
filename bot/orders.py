from bot.logging_config import logger
import time

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Request: {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        order_id = response["orderId"]

        # wait briefly then fetch updated order
        time.sleep(2)

        updated = client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

        logger.info(f"Updated Response: {updated}")
        return updated

    except Exception as e:
        logger.error(str(e))
        raise