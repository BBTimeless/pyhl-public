import pandas as pd 

VIEW_FEATURE_EXCLUDES = ['id', 'teamid']
DATA = pd.read_csv('static/data/data_skater.csv')
MIN_GAMES = 10


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

'''
Calculates the nhl average for metrics: goals per game, assists per game, shots per game, and points per game.

These values are then added to the skater data. The skater data CSV file is opened, modified, and closed with the new data.
'''
def add_skater_averages_to_csv():
    min_games = 10

    # Goals per game average. We dont want players with less than the min games because they can skew the averages.
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

    # Create new columns for metric differences and calculate the new values for said columns.
    data_add_df = DATA.assign(GPGDIF=0.0,APGDIF=0.0,SPGDIF=0.0, PPGDIF=0.0)
    for index, row in data_add_df.iterrows():
        if row['games'] < min_games:
            print('Minimum games not reached:', row['playername'])
            data_add_df = data_add_df.drop(index)
        else:
            if row['position'] == 'Defenseman':
                data_add_df.at[index,'GPGDIF'] = round((row['GPG'] - defense_gpg_avg), 2)
                data_add_df.at[index,'APGDIF'] = round((row['APG'] - defense_apg_avg), 2)
                data_add_df.at[index,'SPGDIF'] = round((row['SPG'] - defense_spg_avg), 2)
                data_add_df.at[index,'PPGDIF'] = round((row['PPG'] - defense_ppg_avg), 2)

            if row['position'] == ('Left Wing' or 'Right Wing'):
                data_add_df.at[index,'GPGDIF'] = round((row['GPG'] - wing_gpg_avg), 2)
                data_add_df.at[index,'APGDIF'] = round((row['APG'] - wing_apg_avg), 2)
                data_add_df.at[index,'SPGDIF'] = round((row['SPG'] - wing_spg_avg), 2)
                data_add_df.at[index,'PPGDIF'] = round((row['PPG'] - wing_ppg_avg), 2)
            
            if row['position'] == 'Center':
                data_add_df.at[index,'GPGDIF'] = round((row['GPG'] - center_gpg_avg), 2)
                data_add_df.at[index,'APGDIF'] = round((row['APG'] - center_apg_avg), 2)
                data_add_df.at[index,'SPGDIF'] = round((row['SPG'] - center_spg_avg), 2)
                data_add_df.at[index,'PPGDIF'] = round((row['PPG'] - center_ppg_avg), 2)

    # Write the new DF to the CSV file.
    data_add_df.to_csv('static/data/data_skater.csv', encoding='utf-8', index=False)