from ytmusic_extract import *

if "youtube" in sys.argv[1]:
    print("yotube url...")
    artist_name, song_name = get_yt_song_info(sys.argv[1])
    
    print("Artist: ", artist_name)
    print("Song: ", song_name)
else:
    print("url not supported")