'''
This module is built to connect to the binance api using .env creds. Once connected, trade orders are recieved in real time.
'''
from imports import *

import numpy

SOCKET = "wss://stream.binance.us:9443/ws/ethusd@trade"
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05

closes = []
in_position = False

client = Client(API_KEY, API_SECRET, tld='us')

def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True

    
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, in_position
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    # candle = json_message['k']

    # is_candle_closed = candle['x']
    # close = candle['c']












    # if is_candle_closed:
    #     print("candle closed at {}".format(close))
    #     closes.append(float(close))
    #     print("closes")
    #     print(closes)

    #     if len(closes) > RSI_PERIOD:
    #         np_closes = numpy.array(closes)
    #         rsi = talib.RSI(np_closes, RSI_PERIOD)
    #         print("all rsis calculated so far")
    #         print(rsi)
    #         last_rsi = rsi[-1]
    #         print("the current rsi is {}".format(last_rsi))

    #         if last_rsi > RSI_OVERBOUGHT:
    #             if in_position:
    #                 print("Overbought! Sell! Sell! Sell!")
    #                 # put binance sell logic here
    #                 order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
    #                 if order_succeeded:
    #                     in_position = False
    #             else:
    #                 print("It is overbought, but we don't own any. Nothing to do.")
            
    #         if last_rsi < RSI_OVERSOLD:
    #             if in_position:
    #                 print("It is oversold, but you already own it, nothing to do.")
    #             else:
    #                 print("Oversold! Buy! Buy! Buy!")
    #                 # put binance buy order logic here
    #                 order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
    #                 if order_succeeded:
    #                     in_position = True

                
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()


def acquire_items():
	'''
	func doc string
	'''
	if os.path.exists('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/items.csv'):
		print('cached csv')
		df = pd.read_csv('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/items.csv')
		return df
	else:
		domain = 'https://api.data.codeup.com'
		endpoint = '/api/v1/items'
		items = []
		while True:
			url = domain + endpoint
			response = requests.get(url)
			data = response.json()
			items.extend(data['payload']['items'])
			endpoint = data['payload']['next_page']
			if endpoint == None:
				items=pd.DataFrame(items)
				items.to_csv('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/items.csv', index=False)
				return items
			else:
				continue
				
def acquire_stores():
	'''
	func doc string
	'''
	if os.path.exists('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/stores.csv'):
		print('cached csv')
		df = pd.read_csv('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/stores.csv')
		return df
	else:
		domain = 'https://api.data.codeup.com'
		endpoint = '/api/v1/stores'
		stores = []
		while True:
			url = domain + endpoint
			response = requests.get(url)
			data = response.json()
			stores.extend(data['payload']['stores'])
			endpoint = data['payload']['next_page']
			if endpoint == None:
				stores=pd.DataFrame(stores)
				stores.to_csv('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/stores.csv', index=False)
				return stores
			else:
				continue

def acquire_sales():
	'''
	func doc string
	'''
	if os.path.exists('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/sales.csv'):
		print('cached csv')
		df = pd.read_csv('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/sales.csv')
		return df
	else:
		domain = 'https://api.data.codeup.com'
		endpoint = '/api/v1/sales'
		sales = []
		while True:
			url = domain + endpoint
			response = requests.get(url)
			data = response.json()
			sales.extend(data['payload']['sales'])
			endpoint = data['payload']['next_page']
			if endpoint == None:
				sales=pd.DataFrame(sales)
				sales.to_csv('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/sales.csv', index=False)
				return sales
			else:
				continue

def merge_on_sales():
	stores=acquire_stores()
	items=acquire_items()
	sales=acquire_sales()

	sales = sales.rename(columns={'item': 'item_id', 'store': 'store_id'})
	sales=sales.merge(items,on='item_id')
	sales=sales.merge(stores,on='store_id')

	return sales

def de_elec():
	de_elec=pd.read_csv('/Users/hinzlehome/codeup-data-science/time-series-exercises/csvs/opsd_germany_daily.csv')
	return de_elec	