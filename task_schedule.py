import json
import requests
import pandas as pd
from datetime import datetime, timedelta

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
            game_data['gamedate'] = format_date(game['gameDate'])
            game_data['homeid'] = game['teams']['home']['team']['id']
            game_data['awayid'] = game['teams']['away']['team']['id']
            games_data_all.append(game_data)
    return(games_data_all)

'''
Writes the schedule data to a csv. This file will be used by the front end to develop views.
'''
def write_game_schedule():
    df = pd.DataFrame(get_game_schedule())
    df.to_csv('static/data/data_schedule.csv', encoding='utf-8', index=False)

'''
Helper function to format the date string into an easier to read format.

Converts from UTC to EST to align with personal use case.
'''
def format_date(date_string):
    dt_string_formatted = date_string.replace('T', ' ')
    dt_string_formatted = dt_string_formatted.replace('Z', ' UTC')

    dt_obj = datetime.strptime(dt_string_formatted, '%Y-%m-%d %H:%M:%S %Z')
    est = dt_obj - timedelta(hours=4)

    final_db_dt_entry = est.strftime('%Y-%m-%d %H:%M:%S')

    return(final_db_dt_entry)