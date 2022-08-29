"""
@author: Noah Horsley
"""


import datetime as dt
import json
import pandas as pd
import requests
from config import Config
from pipe.utils import export


today_date = dt.datetime.today().strftime("%m-%d-%Y %H:%M:%S")
authorization = {
    'Accept': 'application/json',
    'authorization': f'Bearer {Config.CLASH_API_KEY}'
}


def get_clan_data(clantag):
    url = 'https://api.clashofclans.com/v1/clans/%23{}/members'.format(clantag)
    response = requests.get(url, headers=authorization).text
    js = json.loads(response)['items']
    df = pd.DataFrame(js)
    return df


def get_player_data(playertag):
    url = 'https://api.clashofclans.com/v1/players/%23{}'.format(playertag)
    response = requests.get(url, headers=authorization).text
    js = json.loads(response)
    df = pd.DataFrame.from_dict(js, orient='index')
    return df


def get_clash_data(clantag):
    clan_data = get_clan_data(clantag=clantag)
    player_data = pd.DataFrame()
    tags = clan_data['tag'].apply(lambda x: x.replace('#', '', 1)).tolist()
    for tag in tags:
        player_data = pd.concat([player_data, get_player_data(playertag=tag).T])
    export(clan_data, "data/clan_data/clan_data.csv", timestamped_copy=True)
    export(player_data, "data/player_data/player_data.csv", timestamped_copy=True)
    return clan_data, player_data


if __name__ == '__main__':
    test_clantag = 'YQLJ9CRU'
    test_clan_data, test_player_data = get_clash_data(clantag=test_clantag)
    print(test_clan_data.sample(5))
    print(test_player_data.sample(5))
