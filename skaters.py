import pandas as pd 

DATA = pd.read_csv('static/data/data_skater.csv')

'''
Fetches skater data from the CSV file via a list of skater ids. The data is then returned in a list.
'''
def get_skater_data_by_id(player_ids):
    skaters = DATA.loc[DATA['id'].isin(player_ids)]
    return(skaters)

'''
Fetches skater data from the CSV file via a list of team ids. The data is then returned in a list.
'''
def get_skater_data_by_team_id(team_ids):
    skaters = DATA.loc[DATA['currentteamid'].isin(team_ids)]
    return(skaters)

def get_top_skaters(number, feature):
    skaters = DATA.sort_values(by=[feature])
    return(skaters)