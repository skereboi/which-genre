import sys
# Get the HTTP code of the webpage
import requests
# JSON Handler
import json
# Regular Expresions Handler
import re

def get_yt_song_info(youtube_url):
    song_name = None
    artist_name = None

    req = requests.get(youtube_url)
    print(req.text)

#    raw_matches = re.findall('(\{"metadataRowRenderer":.*?\})(?=,{"metadataRowRenderer")', req.text)
#    print(raw_matches)


get_yt_song_info(sys.argv[1])