import pandas as pd

from old.api import ClanRequest, PlayerRequest
from old.entities import Clan, Player


def get_clan_members(clan: Clan) -> list[Player]:
    request = ClanRequest(url_key='clan__members', tag=clan.tag) 
    clan_json = request.request_json()
    member_json = clan_json['items']
    member_tags = [member['tag'].replace('#', '') for member in member_json]
    return [Player(tag=tag) for tag in member_tags]


def get_player_info(player: Player) -> pd.DataFrame:
    request = PlayerRequest(url_key='player__info', tag=player.tag)
    player_json = request.request_json()
    return pd.json_normalize(player_json)  


if __name__ == '__main__':
    clan = Clan('YQLJ9CRU')
    members = get_clan_members(clan) 
    member_data = []
    for member in members:
        member_data.append(get_player_info(member))
    member_df = pd.concat(member_data).reset_index()
    member_df = member_df[['name', 'attackWins', 'donations', 'donationsReceived']]
    print(member_df.sort_values(by='attackWins', ascending=False).tail(15))
    
