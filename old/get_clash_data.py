import json
import pandas as pd
import requests

from config import Config
from old import utilities 


AUTHORIZATION = {
    'Accept': 'application/json',
    'authorization': f'Bearer {Config.CLASH_API_KEY}'
}


def request_clan_data(clan_tag: str) -> pd.DataFrame:
    """
    Request clan data from Clash of Clans API.
    Args:
        clan_tag (str): Clan tag.
    """
    url = 'https://api.clashofclans.com/v1/clans/%23{}/members'.format(clan_tag)
    response = requests.get(url, headers=AUTHORIZATION).text
    js = json.loads(response)['items']
    df = pd.DataFrame(js)
    return df


def extract_player_tags(clan_data: pd.DataFrame) -> list[str]:
    """
    Extract player tags from clan data.
    Args:
        clan_data (pd.DataFrame): Clan data.
    """
    player_tags = clan_data['tag'].apply(lambda x: x.replace('#', '', 1))
    return player_tags.tolist()


def request_player_data(player_tag: str) -> pd.DataFrame:
    """
    Request player data from Clash of Clans API.
    Args:
        player_tag (str): Player tag.
    """
    url = 'https://api.clashofclans.com/v1/players/%23{}'.format(player_tag)
    response = requests.get(url, headers=authorization).text
    js = json.loads(response)
    df = pd.DataFrame.from_dict(js, orient='index')
    return df


def request_clan_player_data(clan_tag: pd.DataFrame) -> pd.DataFrame:
    """
    Get player data for all players in clan.
    Args:
        clan_tag (pd.DataFrame): Clan tag.
    """
    clan_data = request_clan_data(clan_tag)
    player_data = []
    player_tags = extract_player_tags(clan_data)
    for tag in player_tags:
        players.append(request_player_data(tag))
    return player_data


def main(clan_tag: str) -> pd.DataFrame:
    """
    Request and export player data for all players in clan.
    Args:
        clan_tag (str): Clan tag.
    """
    player_data = request_clan_player_data(clan_tag)
    utilities.export(player_data, 
                     "data/player_data/player_data.csv",
                     timestamped_copy=True)
    return player_data


if __name__ == '__main__':
    test_clantag = 'YQLJ9CRU'
    test_player_data = main(test_clantag)
    print(test_player_data.sample(5))

