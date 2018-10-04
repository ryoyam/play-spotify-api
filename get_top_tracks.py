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
    results = sp.current_user_top_tracks(limit=50, time_range='long_term')
    tracks = results['items']
    for i, track in enumerate(tracks):
        album = track['album']['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        print('{i}: {track_name} by {artists}'.format(i=i, track_name=track['name'], artists=artists))
else:
    print("Can't get token for", user)
