import os
import sys
import time
import signal
from models.exchange.coinbase_pro import WebSocketClient as CWebSocketClient


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def handler(signum, frame):
    if signum == 2:
        print(" -> not finished yet!")
        return


try:
    websocket = CWebSocketClient(
        [
            "ADA-GBP",
            # "BCH-GBP",
            # "BTC-GBP",
            # "ETH-GBP",
            # "LTC-GBP",
            # "MATIC-GBP",
            # "SOL-GBP",
            # "XLM-EUR",
        ]
    )
    websocket.start()
    message_count = 0
    while True:
        if websocket:
            if (
                message_count != websocket.message_count
                and websocket.tickers is not None
            ):
                cls()
                print("\nMessageCount =", "%i \n" % websocket.message_count)
                # print(websocket.candles_1m)
                # print(websocket.candles_5m)
                # print(websocket.candles_15m)
                print(websocket.candles_1h)
                # print(websocket.candles_6h)
                # print(websocket.candles_1d)
                message_count = websocket.message_count
                time.sleep(5)  # output every 5 seconds, websocket is realtime

# catches a keyboard break of app, exits gracefully
except KeyboardInterrupt:
    signal.signal(signal.SIGINT, handler)
    print("\nPlease wait while threads complete gracefully.")
    websocket.close()
    sys.exit(0)