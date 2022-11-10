import pandas as pd 

VIEW_FEATURE_EXCLUDES = ['id', 'teamid']
DATA = pd.read_csv('static/data/data_skater.csv')


'''
Fetches skater data from the CSV file via a list of skater ids. The data is then returned in a list.
'''
def get_skater_data_by_id(player_ids):
    skaters = DATA.loc[DATA['id'].isin(player_ids)]
    skaters = skaters.drop(columns=VIEW_FEATURE_EXCLUDES)
    return(skaters)

'''
Fetches skater data from the CSV file via a list of team ids. The data is then returned in a list.
'''
def get_skater_data_by_team_id(team_ids):
    skaters = DATA.loc[DATA['teamid'].isin(team_ids)]
    skaters = skaters.drop(columns=VIEW_FEATURE_EXCLUDES)
    return(skaters)

def get_top_skaters(number, feature):
    skaters = DATA.sort_values(by=[feature])
    skaters = skaters.drop(columns=VIEW_FEATURE_EXCLUDES)
    return(skaters)

def add_skater_averages():
    min_games = 10

    # Goals per game average
    wing_data_gpg = DATA.loc[(DATA['games'] >= min_games) & ((DATA['position'] == 'Left Wing') | (DATA['position'] == 'Right Wing'))]
    wing_gpg_avg = wing_data_gpg['GPG'].mean()

    center_data_gpg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Center')]
    center_gpg_avg = center_data_gpg['GPG'].mean()

    defense_data_gpg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Defenseman')]
    defense_gpg_avg = defense_data_gpg['GPG'].mean()

    # Assists per game average
    wing_data_apg = DATA.loc[(DATA['games'] >= min_games) & ((DATA['position'] == 'Left Wing') | (DATA['position'] == 'Right Wing'))]
    wing_apg_avg = wing_data_apg['APG'].mean()

    center_data_apg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Center')]
    center_apg_avg = center_data_apg['APG'].mean()

    defense_data_apg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Defenseman')]
    defense_apg_avg = defense_data_apg['APG'].mean()

    # Shots per game average
    wing_data_spg = DATA.loc[(DATA['games'] >= min_games) & ((DATA['position'] == 'Left Wing') | (DATA['position'] == 'Right Wing'))]
    wing_spg_avg = wing_data_spg['SPG'].mean()

    center_data_spg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Center')]
    center_spg_avg = center_data_spg['SPG'].mean()

    defense_data_spg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Defenseman')]
    defense_spg_avg = defense_data_spg['SPG'].mean()

    #Points per game average 
    wing_data_ppg = DATA.loc[(DATA['games'] >= min_games) & ((DATA['position'] == 'Left Wing') | (DATA['position'] == 'Right Wing'))]
    wing_ppg_avg = wing_data_ppg['PPG'].mean()

    center_data_ppg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Center')]
    center_ppg_avg = center_data_ppg['PPG'].mean()

    defense_data_ppg = DATA.loc[(DATA['games'] >= min_games) & (DATA['position'] == 'Defenseman')]
    defense_ppg_avg = defense_data_ppg['PPG'].mean()

    # ppg_avg = min_games_data['PPG'].mean()
    
    print('Wing gpg_avg', wing_gpg_avg)
    print('center_gpg_avg', center_gpg_avg)
    print('defense_gpg_avg', defense_gpg_avg)

    print('wing_apg_avg', wing_apg_avg)
    print('center_apg_avg', center_apg_avg)
    print('defense_apg_avg', defense_apg_avg)

    print('wing_spg_avg', wing_spg_avg)
    print('center_spg_avg', center_spg_avg)
    print('defense_spg_avg', defense_spg_avg)
    
    print('wing_ppg_avg', wing_ppg_avg)
    print('center_ppg_avg', center_ppg_avg)
    print('defense_ppg_avg', defense_ppg_avg)



add_skater_averages()