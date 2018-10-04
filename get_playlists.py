# https://spotipy.readthedocs.io/en/latest/#authorization-code-flow

import sys
import spotipy
import spotipy.util as util
import json


scope = 'playlist-read-private' #'user-top-read'



if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope) # using SPOTIPY_XXX enviroment variables


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playlists()

    path = './playlists.json'
    with open(path, 'w') as f:
        json.dump(results, f, indent=4) 
# results = sp.current_user_top_tracks()
    # for item in results['items']:
    #    track = item['track']
    #     print(track['name'] + ' - ' + track['artists'][0]['name'])


else:
    print("Can't get token for", user)
