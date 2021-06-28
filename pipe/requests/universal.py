# import global packages
import json
import os
import pandas as pd
import requests
import sys

# locate root dir
flare = '\\flare.py'
path = os.getcwd()
while not os.path.isfile(path + flare):
    path = os.path.dirname(path)
sys.path.append(path)

# import local packages/objects
from pipe.authorization.clash_api import retrieve_api_key


def make_api_request(url=str, key=str):
    response = requests.get(url, key).text
    return response

def load_and_stage(response):
    js = json.loads(response)['items']
    df = pd.DataFrame(js)
    return df
    
def get_clan_information(url):
    key = retrieve_api_key()
    response = make_api_request(url, key)
    df = load_and_stage(response)
    return df


"""Need to turn key into proper authorization header.

"""