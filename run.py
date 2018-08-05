import random
import requests
from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

from config import *

api = ViaBTCAPI(EXCHANGE_URL)

def get_btc_eth_price(url=BTC_ETH_PRICE_URL):
    resp = requests.get(url)
    price = float(resp.json()["BTC"])
    mult = 1 + BTC_ETH_PRICE_ERROR_PRC / 100 * 2 * (random.random() - 0.5)
    return price * mult

def get_balance(api, user_id=BOT_USER_ID):
    return api.balance_query(user_id)["result"]

def get_orderbook(api, market=MARKET_NAME):
    return api.order_depth(market)["result"]

def put_order(api, action, amount, price):
    return api.order_put_limit(
        user_id=BOT_USER_ID,
        market=MARKET_NAME,
        side=action,
        amount=amount,
        price=price
    )

balances = get_balance(api)
print("My balance: {0} {1}, {2} {3}".format(
    balances[MONEY_NAME]["available"], MONEY_NAME, balances[STOCK_NAME]["available"], STOCK_NAME
))

current_btc_eth_price = get_btc_eth_price()
print("Current BTCETH price: {}".format(current_btc_eth_price))

action = "BUY" if random.random() > BOT_BUY_PROB else "SELL"
direction = action != "SELL"

spread = current_btc_eth_price * BOT_SPREAD_PRC / 100
price_delta = (-1) ** direction * random.random() * spread
price = current_btc_eth_price + price_delta 

asset_name_to_trade = MONEY_NAME if action == "BUY" else STOCK_NAME
amount = float(balances[asset_name_to_trade]["available"]) * BOT_TRADE_BALANCE_PRC / 100
print("Going to {} {} {} for {} {}".format(action, amount, STOCK_NAME, price, MONEY_NAME))
resp = put_order(api, action, amount, price)
if resp["error"] is not None:
    print(resp["error"]["message"])
print()

