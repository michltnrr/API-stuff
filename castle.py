import requests
import json
params = {'User-Agent': 'yourchess.com email'}
response = requests.get('https://api.chess.com/pub/player/{personsusername}', headers=params)

user_data = (response.json())
print(user_data['username'], user_data['country'][-2:])
response = requests.get('https://api.chess.com/pub/player/{personsusername}/stats', headers=params)
user_stats = response.json()

print(user_stats['chess_blitz']['last']['rating'])
print(user_stats['chess_blitz']['record'])
