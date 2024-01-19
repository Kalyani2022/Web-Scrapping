from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from collections import Counter
import pandas as pd


def get_channel_results():
    driver = webdriver.Edge()
    driver.get(channel_url)

    title = driver.title
    print(f'{title}\\n')

    list = []

    link_data = driver.find_elements(By.XPATH, '//*[@id="meta"]//a')
    for x in link_data:
        link = x.get_attribute('href')
        list.append(link)

    # print(f'\n{link}')
    return list
    

# Main script
channel_url = 'https://www.youtube.com/@tseries/videos'
video_list = get_channel_results()

print(video_list, '\n', len(video_list))

url_format = 'https://www.youtube.com/watch?v='

df = pd.DataFrame(columns=['LINKS'])
df['LINKS'] = video_list
print("Dataframe : \n", df)
df.to_csv('tseries_playlists.csv', index=False)
print("Playlist extracted successfully")

for i in range(0, len(df)):
    lnk = str(df.loc[i]['LINKS'])
    if url_format in lnk:
        video_id = lnk.split('=')[1]
    
        char_counts = Counter(video_id.lower())
        print(f"Video ID of v{i} = {video_id}")
        print()
        max_char = max(char_counts, key=char_counts.get)
        print(f"Key: {max_char}, Value: {char_counts[max_char]}\n")
