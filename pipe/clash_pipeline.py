# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:21:31 2020

@author: Noah Horsley
"""
# %%
# setup
import datetime as dt
import json
import pandas as pd
import requests

timestamp = dt.datetime.today().strftime("%m-%d-20%y %H:%M:%S")
authorization = {
    'Accept':'application/json',
    'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9. \
     eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjdmNDRmMzUzLTU0ZDgtNDM2Yi05YWE5LTFhMmU5NTAwODJmNiIsI \
     mlhdCI6MTYxNjc5MzUwMSwic3ViIjoiZGV2ZWxvcGVyL2RlMTE5MTZkLWI4ZDktNjcwYi04MmZlLTdjOGRjYzQ4MjE3NiIsInNjb3BlcyI6WyJjbGFzaCJd \
     LCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjczLjEzNy4xMTMuMTgiXSwidHlwZ \
     SI6ImNsaWVudCJ9XX0.UNVMbZtklvMnE7-fxaup-VzeVSU3VzJ0UQb-md2T0QoJoETrg2noWd9e0kQOZMP1Y6Vq1-gmRKsDGh_eUvvJYg'
}

# %%
# functions
def get_clan_data(clantag):
    response = requests.get('https://api.clashofclans.com/v1/clans/%23{}/members'.format(clantag), headers=authorization).text
    js = json.loads(response)['items']
    df = pd.DataFrame(js)
    return df

def get_player_data(playertag):
    response = requests.get('https://api.clashofclans.com/v1/players/%23{}'.format(playertag), headers=authorization).text
    js = json.loads(response)
    df = pd.DataFrame.from_dict(js, orient='index')
    return df

def pull_from_api(clantag):
    clan_data = get_clan_data(clantag=clantag)
    player_data = pd.DataFrame()
    tags = clan_data['tag'].apply(lambda x: x.replace('#', '', 1)).tolist()
    for tag in tags:
        player_data = player_data.append(get_player_data(playertag=tag).T)
    return clan_data, player_data

# %%
# retrieve data
clantag = 'YQLJ9CRU'
clan_data, player_data = pull_from_api(clantag=clantag)