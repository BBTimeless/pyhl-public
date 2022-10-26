import json
import requests

'''
Calls the api and formats a list of dictionaries containing the game schedule.
'''
def get_game_schedule():
    games_data_all = []
    request_string = 'https://statsapi.web.nhl.com/api/v1/schedule?season=20222023'
    schedule_data = json.loads(requests.get(request_string).text)
    dates = schedule_data['dates']
    for date in dates:
        games = date['games']
        for game in games:
            game_data = {}
            game_data['id'] = game['gamePk']
            game_data['gamedate'] = game['gameDate']
            game_data['homeid'] = game['teams']['home']['team']['id']
            game_data['awayid'] = game['teams']['away']['team']['id']
            games_data_all.append(game_data)
    return(games_data_all)

