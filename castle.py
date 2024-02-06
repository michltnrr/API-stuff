import requests
import json
params = {'User-Agent': 'michaeldturner21@gmail.com'}
response = requests.get('https://api.chess.com/pub/player/macmike69', headers=params)
# print(response.status_code)
user_data = (response.json())
# print(user_data)
print(user_data['username'], user_data['country'][-2:])
response = requests.get('https://api.chess.com/pub/player/macmike69/stats', headers=params)
user_stats = response.json()
# print(user_stats)
# print(user_stats['chess_blitz'])
print(user_stats['chess_blitz']['last']['rating'])
print(user_stats['chess_blitz']['record'])