import os
import requests

API_KEY = os.getenv('TRACKER_API_KEY')
BASE_URL = 'https://public-api.tracker.gg/v2/apex/standard/profile'

def get_game_stats(player_name):
    headers = {
        'TRN-Api-Key': API_KEY,
    }
    params = {
        'platform': 'PC',
        'name': player_name,
    }
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        stats = data['segments'][0]['stats']
        return f"{player_name}'s stats: {stats['kills']['displayValue']} kills, {stats['damage']['displayValue']} damage"
    else:
        return 'Error retrieving game stats'
