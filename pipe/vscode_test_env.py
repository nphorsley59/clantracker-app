# import global packages
import os
import sys

# locate root dir
flare = '\\flare.py'
path = os.getcwd()
while not os.path.isfile(path + flare):
    path = os.path.dirname(path)
sys.path.append(path)

# import local packages/objects
from pipe.authorization.clash_api import *
from pipe.requests.clans import Clan
from pipe.requests.universal import *


Bloodline = Clan('#YQLJ9CRU')
print(make_api_request(Bloodline.convert_to_url(), retrieve_api_key()))

