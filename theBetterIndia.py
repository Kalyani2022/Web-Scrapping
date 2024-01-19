from bs4 import BeautifulSoup
import requests as req
import pandas as pd

pd.set_option('display.width',2000)
pd.set_option('display.max_columns',1000)
df = pd.DataFrame(columns = ['TITLE','AUTHOR','URL'])

for page_no in range(1,900):
  source = req.get(f'https://www.thebetterindia.com/stories/page/{page_no}/').text
  soup = BeautifulSoup(source,'lxml')

  #print(f'\n\n <========= {page_no} ==========>')

  for article in soup.find_all('article'):
    title_section = article.div.find('h3',class_="elementor-post__title")
    title = title_section.a.text
    url = title_section.a['href']
    author = article.div.find('span',class_="elementor-post-author").text
    df = df.append({'TITLE' : title.strip(), 'AUTHOR' : author.strip() , 'URL' : url.strip()},ignore_index=True)
  print(df)

tbi_csv_data = df.to_csv('tbi.csv',index = False)
print(tbi_csv_data)


'''
how to use concat function ,when values added in database ?
How to add cat-title, author and published date ?

from bs4 import BeautifulSoup
import requests

source1 = requests.get(f'https://www.thebetterindia.com/topics/education/').text
soup1 = BeautifulSoup(source1,'lxml')

for article in soup1.find_all('article'):
  title = article.div.find('h3',class_="entry-title").a.text
  url = article.div.find('h3',class_="entry-title").a['href']
  print(title,' | ',url)

  source2 = requests.get('https://www.thebetterindia.com/275433/coding-for-children-online-classes-benefits-parenting-tips/').text
  soup2 = BeautifulSoup(source2,'lxml')

  article1 = soup2.find('article')
  cat_title = article1.div.a.text
  author = article1.div.ul.li[0].text
  pub_date = article1.div.ul.li[1].text
  print(cat_title,' | ',author,' | ',pub_date)
'''
