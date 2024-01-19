from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('https://www.moneycontrol.com/').text
soup = BeautifulSoup(source, 'lxml')

indices = soup.find('div', id='market_action')

for table in indices.find_all('table', class_='rhsglTbl'):
	for col in table.find_all('th'):
		col = col.text
		print(col, end = ' | ')

	try:
		body = table.find('tbody')
		for row in body.find_all('tr'):
			print()
			for col in row.find_all('td'):
				try:
					val = col.text
					print(val.strip(), end=' | ')
				except Exception as e:
					pass
	except:
		pass