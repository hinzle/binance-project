'''
This module is built to connect to the binance api using .env creds. Once connected, trade orders are recieved in real time.
'''
from imports import *

SOCKET = "wss://stream.binance.us:9443/ws/ethusd@trade"
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05
client = Client(API_KEY, API_SECRET, tld='us')

closes = []
in_position = False

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, in_position
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
