# import global packages
from configparser import ConfigParser
import os
import sys

# locate root dir
beacon = '\\beacon.py'
path = os.getcwd()
while not os.path.isfile(os.path.join(path, beacon)):
    path = os.path.dirname(path)
sys.path.append(path)

# import local packages/objects
from definitions import CONFIG_PATH


def retrieve_api_key(config_path=CONFIG_PATH):
    config = ConfigParser()
    config.read(config_path)
    key = config.get('api_access', 'access_key')
    return key


""" Consider adding a Class of functions that retreive data from 
config file. """