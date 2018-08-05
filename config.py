import os

EXCHANGE_URL = "http://localhost:8080/"
MARKET_NAME = "TESTNET3RINKEBY"
MONEY_NAME = "TESTNET3"
STOCK_NAME = "RINKEBY"
BTC_ETH_PRICE_URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC"
BTC_ETH_PRICE_ERROR_PRC = float(os.getenv('BTC_ETH_PRICE_ERROR_PRC', 0))

BOT_USER_ID = int(os.getenv('BOT_USER_ID', -666))
BOT_TRADE_BALANCE_PRC = float(os.getenv('BOT_TRADE_BALANCE_PRC', 1))
BOT_SPREAD_PRC = float(os.getenv('BOT_SPREAD_PRC', 0.1))
BOT_BUY_PROB = float(os.getenv('BOT_BUY_PROB', 0.5))
