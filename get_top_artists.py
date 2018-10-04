# https://spotipy.readthedocs.io/en/latest/#authorization-code-flow

import sys
import spotipy
import spotipy.util as util


scope = 'user-top-read' #'user-top-read'



if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope) # using SPOTIPY_XXX enviroment variables


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_artists(limit=50, time_range='long_term')
    artists = results['items']
    for i, artist in enumerate(artists):
        print('{i}: {artist_name} -- {genre}'.format(i=i, artist_name=artist['name'], genre=' / '.join(artist['genres'])))
else:
    print("Can't get token for", user)
