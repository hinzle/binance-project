# acquire.py
'''
pull the latest 1000 candlestick entries from the binance api
'''
import os
print(os.getcwd())

import sys
local_path = '/Users/hinzlehome/codeup-data-science/binance-project/'
sys.path.insert(0, local_path)
from utils.imports import *




def tidy_btcusd():
	if os.path.exists('/Users/hinzlehome/codeup-data-science/binance-project/csv/btcusd.csv'):
		print('cached csv')
		df = pd.read_csv('/Users/hinzlehome/codeup-data-science/binance-project/csv/btcusd.csv')
		return df
	else:
		payload = {'symbol':'BTCUSD','interval':'1m','limit':'1000'}
		r = requests.get('https://api.binance.us/api/v3/klines', params=payload)
		btcusd_json=r.json()
		btcusd_df=pd.DataFrame(btcusd_json)
		columns=['open_time','open','high','low','close','volume','close_time','quote_asset','number_of_trades','taker_buy_base_asset_vol','taker_buy_quote_asset_vol','ignore']
		btcusd_df.columns=columns
		btcusd_df.to_csv('/Users/hinzlehome/codeup-data-science/binance-project/csv/btcusd.csv', index=False)
		return btcusd_df

def model_btcusd():
	
