import os
import pandas as pd
from config import Config
from pipe.connect_sqlalchemy import get_session
from pipe.sqlalchemy_models import Player


def import_players():
    path = "data/player_data/player_data.csv"
    return pd.read_csv(os.path.join(Config.PROJECT_DIR, path))


def process_players():
    players = import_players()[['tag', 'name', 'role']]
    return players


def insert_players_table():
    players = process_players()
    print(players.to_dict(orient="records"))
    session = get_session()
    session.bulk_insert_mappings(Player, players.to_dict(orient="records"))
    session.commit()


if __name__ == '__main__':
    print(insert_players_table())
