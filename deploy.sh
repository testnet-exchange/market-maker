# kill previous bots
bash kill.sh

export BOT_USER_ID='-1448'; export BTC_ETH_PRICE_ERROR_PRC=15; export BOT_SPREAD_PRC=1; bash run.sh &
export BOT_USER_ID='-777'; export BTC_ETH_PRICE_ERROR_PRC=0.1; export BOT_SPREAD_PRC=0.01; bash run.sh &
export BOT_USER_ID='-1337'; export BTC_ETH_PRICE_ERROR_PRC=10; export BOT_SPREAD_PRC=1; bash run.sh &