import json
import requests
from teams import get_team_ids 

'''
Calls the nhl team api and returns a list of all active player ids.
'''
def get_player_ids():
    player_ids = []

    for team_id in get_team_ids():
        request_string = 'https://statsapi.web.nhl.com/api/v1/teams/{}/roster'.format(team_id)
        team_roster_data = json.loads(requests.get(request_string).text)

        for player in team_roster_data['roster']:
            player_ids.append(player['person']['id'])
        
    return(player_ids)

'''
Makes a request for each player and records the player statistics.

Returns two lists of player records: [player_stats_skaters, player_stats_goalies]
'''
def get_player_stats():
    player_stats_skaters = []
    player_stats_goalies = []

    for player_id in get_player_ids():
        request_string = 'https://statsapi.web.nhl.com/api/v1/people/{}?hydrate=stats(splits=statsSingleSeason)'.format(player_id)
        player_data = json.loads(requests.get(request_string).text)

        if (player_data['people'][0]['primaryPosition']['abbreviation'] == 'G'):
            record = {}

            # People Info
            log_string = 'Goalie Record Found: {} {}'.format(str(player_data['people'][0]['id']), player_data['people'][0]['fullName'])
            print(log_string)

            record['id'] = player_data['people'][0]['id']
            record['currentteamid'] = player_data['people'][0]['currentTeam']['id']
            record['fullname'] = player_data['people'][0]['fullName']
            record['currentteam'] = player_data['people'][0]['currentTeam']['name']
            record['primaryposition'] = player_data['people'][0]['primaryPosition']['name']
            record['lastupdated'] = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")

            # Stats Info
            # Check for stats
            try:
                stats = player_data['people'][0]['stats'][0]['splits'][0]['stat']
                record['wins'] = stats['wins']
                record['losses'] = stats['losses']
                record['ties'] = stats['ties']
                record['shutouts'] = stats['shutouts']
                record['savepercentage'] = stats['savePercentage']
                record['goalagainstaverage'] = stats['goalAgainstAverage']
            # No Stats (Rookie or First NHL Game)
            except (IndexError, KeyError):
                record['wins'] = None
                record['losses'] = None
                record['ties'] = None
                record['shutouts'] = None
                record['savepercentage'] = None
                record['goalagainstaverage'] = None
            player_stats_goalies.append(record)
            

        else:
            record = {}

            # People Info
            log_string = 'Skater Record Found: {} {}'.format(str(player_data['people'][0]['id']), player_data['people'][0]['fullName'])
            print(log_string)

            record['id'] = player_data['people'][0]['id']
            record['currentteamid'] = player_data['people'][0]['currentTeam']['id']
            record['playername'] = player_data['people'][0]['fullName']
            record['currentteam'] = player_data['people'][0]['currentTeam']['name']
            record['position'] = player_data['people'][0]['primaryPosition']['name']
            record['lastupdated'] = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")

            # Stats Info
            # Check for stats
            try:
                stats = player_data['people'][0]['stats'][0]['splits'][0]['stat']
                record['goals'] = stats['goals']
                record['assists'] = stats['assists']
                record['pim'] = stats['pim']
                record['shots'] = stats['shots']
                record['games'] = stats['games']
                record['hits'] = stats['hits']
                record['powerplaygoals'] = stats['powerPlayGoals']
                record['powerplaypoints'] = stats['powerPlayPoints']
                record['faceoffpct'] = stats['faceOffPct']
                record['blocked'] = stats['blocked']
                record['plusminus'] = stats['plusMinus']
                record['points'] = stats['points']
                record['timeonicepergame'] = float(stats['timeOnIcePerGame'].replace(":", "." ))

            # No Stats (Rookie or First NHL Game)
            except (IndexError, KeyError):
                record['goals'] = None
                record['assists'] = None
                record['pim'] = None
                record['shots'] = None
                record['games'] = None
                record['hits'] = None
                record['powerplaygoals'] = None
                record['powerplaypoints'] = None
                record['faceoffpct'] = None
                record['blocked'] = None
                record['plusminus'] = None
                record['points'] = None
                record['timeonicepergame'] = None
            player_stats_skaters.append(record)
    return(player_stats_skaters, player_stats_goalies)
