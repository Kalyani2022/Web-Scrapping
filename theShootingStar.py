from bs4 import BeautifulSoup
import requests
import pandas as pd

import warnings
warnings.simplefilter(action='ignore')

pd.set_option('display.width',1000)
pd.set_option('display.max_columns',500)
df = pd.DataFrame(columns = ['DATE','TITLE','No_Of_Comments','URL'])

for year in range(2008, 2023):
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

			df = df.append({'DATE':date.strip(),'TITLE':title.strip(),'No_Of_Comments':comments.strip(),'URL':url.strip()},ignore_index =True )
			print(df)
		except:
			pass
			
		#print(title,  ' | ', date, ' | ', comments)
	#print(df)
 
tss_csv_data = df.to_csv('tss.csv')
print(tss_csv_data)