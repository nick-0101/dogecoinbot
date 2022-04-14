import time
import argparse
from binance import Client
from binance.enums import *

# #
# Command line argument parser
# #
parser = argparse.ArgumentParser(
    description='Optional bot arguments.')
parser.add_argument("--time_to_sell", type=int,
                    help="Specify how long until you want the bot to sell the dogecoin")
args = parser.parse_args()

# Send a buy order request


def doge_order_request(client):
    # Get DOGE price
    doge_price = client.get_symbol_ticker(symbol="DOGEUSDT")

    # Calculate how much DOGE $25 can buy
    buy_quantity = round(25 / float(doge_price['price']))

    # Create & Process Order
    try:
        client.create_test_order(
            symbol='DOGEUSDT',
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=buy_quantity
        )
        print('✅ Bought', buy_quantity, 'DOGE at', doge_price['price'] + "\n")

        # Determine how long to wait until selling
        tts_value = args.time_to_sell
        sleep_sec = tts_value * 60

        if sleep_sec >= 240:
            print("🟡 Waiting " + str(tts_value) + " minute/s until selling")
            time.sleep(sleep_sec)

            # Send sell request after tts has finished
            doge_sell_request(client)
        elif sleep_sec < 240:
            print("🟡 Waiting " + str(tts_value) + " minute/s until selling")
            time.sleep(sleep_sec)

            # Send sell request after tts has finished
            doge_sell_request(client)

            # Sleep the difference in time so the program always waits 4 minutes before scanning tweets again
            time.sleep(240 - sleep_sec)
        else:
            return

    except:
        return

# Send a sell order at market price. Market orders are transactions meant to execute as quickly as possible at the current market price.


def doge_sell_request(client):
    # Get DOGE price
    doge_price = client.get_symbol_ticker(symbol="DOGEUSDT")

    # Calculate how much DOGE $25 can sell
    sell_quantity = round(25 / float(doge_price['price']))

    # Create & Process Order
    try:
        client.order_market_sell(
            symbol='DOGEUSDT',
            quantity=sell_quantity
        )
        print('📈 Sold', sell_quantity, 'DOGE at', doge_price['price'] + '\n')
    except:
        return
