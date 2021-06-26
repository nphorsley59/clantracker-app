# import global packages
import json
import os
import pandas as pd
import requests
import sys

# locate root dir
beacon = '\\beacon.py'
path = os.getcwd()
while not os.path.isfile(os.path.join(path, beacon)):
    path = os.path.dirname(path)
sys.path.append(path)

# import local packages/objects
from pipe.authorization.clash_api import retrieve_api_key


class Clan:
    def __init__(self, clantag):
        self.clantag = clantag
        self.members = []


def convert_to_url(clantag):
    first_char = clantag[0]
    if first_char == '#':
        clantag = '%23' + clantag[1:]
    url = f'https://api.clashofclans.com/v1/clans/{clantag}/members'
    return url

def make_api_request(url=str, key=str):
    response = requests.get(url, key).text
    return response

def load_and_stage(response):
    js = json.loads(response)['items']
    df = pd.DataFrame(js)
    return df
    
def get_clan_information(clantag):
    url = convert_to_url(clantag)
    key = retrieve_api_key()
    response = make_api_request(url, key)
    df = load_and_stage(response)
    return df


""" Need to make `convert_to_url` a Class function and call a class object
in `get_clan_information`."""