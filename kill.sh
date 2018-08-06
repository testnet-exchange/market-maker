# kill previous bots
kill $(ps aux | grep 'run_market_maker.py' | grep -v grep | awk '{print $2}')