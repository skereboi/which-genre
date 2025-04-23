import sys
# Get the HTTP code of the webpage
import requests
from bs4 import BeautifulSoup
# JSON Handler
#import json
# Regular Expresions Handler
#import re

def get_yt_song_info(url):
 
    song_name = None
    artist_name = None


    if "music" in url:
        print("music url, replacing...")
        url = url.replace("music","www") 

    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, features="html.parser")

    link = soup.find_all(name="title")[0]
    title = link.text

    title_split = title.split('-')

    artist_name = title_split[0]
    song_name = title_split[1]
    return artist_name, song_name
    