from abc import ABC, abstractmethod
import json
import requests

from config import Config


AUTHORIZATION = {
    'Accept': 'application/json',
    'authorization': f'Bearer {Config.CLASH_API_KEY}'
}

URL_BASE = 'https://api.clashofclans.com/v1/'

URLS = {
    'clan__info': 'clans/%23{clantag}',
    'clan__members': 'clans/%23{clantag}/members',
    'clan__current_war': 'clans/%23{clantag}/currentwar',
    'clan__league_group': 'clans/%23{clantag}/currentwar/leaguegroup',
    'clan__raid_seasons': 'clans/%23{clantag}/capitalraidseasons',
    'player__info': 'players/%23{playertag}',
    'war__clan_war': 'clanwarleagues/wars/%23{wartag}'
}


class Request(ABC):

    def __init__(self, url_key: str, tag: str):
        self.url = self._construct_url(url_key, tag)
    
    @staticmethod
    @abstractmethod
    def _construct_url(url_key: str, tag: str) -> str:
        pass

    def request_json(self) -> dict:
        response = requests.get(self.url, headers=AUTHORIZATION)
        response.raise_for_status()
        return json.loads(response.text)


class ClanRequest(Request):

    @staticmethod
    def _construct_url(url_key: str, tag: str) -> str:
        return URL_BASE + URLS[url_key].format(clantag=tag)


class PlayerRequest(Request):

    @staticmethod
    def _construct_url(url_key: str, tag: str) -> str:
        return URL_BASE + URLS[url_key].format(playertag=tag)


class WarRequest(Request):

    @staticmethod
    def _construct_url(url_key: str, tag: str) -> str:
        return URL_BASE + URLS[url_key].format(wartag=tag)

