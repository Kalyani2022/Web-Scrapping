from bs4 import BeautifulSoup
import requests
import snoop

import warnings
warnings.simplefilter(action='ignore')

from threading import *
import time

class Hello_tss(Thread):
	@snoop
	def run(self):
		dct = {}
		lst = []
		for year in range(2008, 2012):
			source = requests.get(f"https://the-shooting-star.com/{year}/").text
			soup = BeautifulSoup(source, 'lxml')

			#print(f"\n\nBlogs published in {year}::========>")

			for article in soup.find_all('article'):
				title = url = date = comments = None

				try:
					title_section = article.h2.a

					title = title_section.text
					dct['TITLE'].append(title).strip()

					url = title_section['href']
					dct['URL'].append(url).strip()

					date = article.find('div', class_='entry-date').a.text
					dct['DATE'].append(date).strip()

					comments = article.find('div', class_='entry-comments').a.text.split(' ')[1]
					dct['COMMENTS'].append(comments).strip()

					print(dct)

					#l = dict(zip([Key],[value]))
					'''
					lst =[[dict(zip(['TITLE'],[title])),
					dict(zip(['URL'],[url])),
					dict(zip(['DATE'],[date])),
					dict(zip(['COMMENTS'],[comments]))
					]]

					#lst = list.append(dct,ignore_index =True )
					print(lst)
					'''

				except:
					pass
		
		#tss_csv_data = lst.to_csv('tss.csv')
		#print(tss_csv_data)

class Hi_tss(Thread):
	@snoop	
	def run(self):
		
		lst =[]

		for year in range(2013, 2017):
			source = requests.get(f"https://the-shooting-star.com/{year}/").text
			soup = BeautifulSoup(source, 'lxml')

			#print(f"\n\nBlogs published in {year}::========>")

			for article in soup.find_all('article'):
				title = url = date = comments = None

				try:
					title_section = article.h2.a
					title = title_section.text
					url = title_section['href']

					date = article.find('div', class_='entry-date').a.text
					comments = article.find('div', class_='entry-comments').a.text.split(' ')[1]

					lst = lst.append({'DATE':date.strip(),'TITLE':title.strip(),'No_Of_Comments':comments.strip(),'URL':url.strip()},ignore_index =True )
					print(lst)
				except:
					pass
		
		#tss_csv_data = lst.to_csv('tss.csv')
		#print(tss_csv_data)

class Hola_tss(Thread):
	@snoop
	def run(self):
		
		lst = []

		for year in range(2018, 2023):
			source = requests.get(f"https://the-shooting-star.com/{year}/").text
			soup = BeautifulSoup(source, 'lxml')

			#print(f"\n\nBlogs published in {year}::========>")

			for article in soup.find_all('article'):
				title = url = date = comments = None

				try:
					title_section = article.h2.a
					title = title_section.text
					url = title_section['href']

					date = article.find('div', class_='entry-date').a.text
					comments = article.find('div', class_='entry-comments').a.text.split(' ')[1]

					lst = lst.append({'DATE':date.strip(),'TITLE':title.strip(),'No_Of_Comments':comments.strip(),'URL':url.strip()},ignore_index =True )
					print(lst)
				except:
					pass
		
		#tss_csv_data = lst.to_csv('tss.csv')
		#print(tss_csv_data)


start = time.time()
h1 = Hello_tss()
h2 = Hi_tss()
h3 = Hola_tss()

h1.start()
time.sleep(0.1)
h2.start()
time.sleep(0.1)
h3.start()

h1.join()
h2.join()
h3.join()

print("Bye")
print(f"Total time taken = {time.time() - start}")

