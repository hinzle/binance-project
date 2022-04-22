'''
This module is built to pull HEB store, item, and sales data. The three tables are then merged.
'''

import sys
sys.path.insert(0, '/Users/hinzlehome/codeup-data-science/time-series-exercises/utils')
from imports import *

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