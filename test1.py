import pandas as pd
import numpy as np
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from config import CLIENT_ID
from config import CLIENT_SECRET

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])                                                           