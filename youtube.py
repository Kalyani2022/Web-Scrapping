import requests
from bs4 import BeautifulSoup
import scrapetube
import pandas as pd
from collections import Counter

videos = scrapetube.get_channel(channel_url= 'https://www.youtube.com/@tseries/videos')
list = []
df = pd.DataFrame(columns=['URL'])
url = 'https://www.youtube.com/watch?v='

for video in videos:
    link = url + str(video['videoId'])
    print(link)
    list.append(link)

df = pd.DataFrame(columns= ['LINKS'])
df['LINKS'] = list
df.to_csv('tseries_playlists.csv')
print("Playlist extracted successfully")

for i in range(0, len(df)):
    lnk = df.loc[i]
    strng = str(lnk).split('=')[1].rstrip('\nName: 0, dtype: object')
    char_counts = Counter(strng.lower())
    print(f"Video ID of v[{i}] = ", strng)

    # for char, count in char_counts.items():
    #     print(f"Key: {char} Value: {count}")

    max_char = max(char_counts, key=char_counts.get)
    print(f"\nkey: {max_char}, Value: {char_counts[max_char]}")
    print()