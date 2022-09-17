import ast
import os

import pandas as pd
import pangres
from sqlalchemy import String

from config import Config
from old.connect_sqlalchemy import get_engine


def import_players():
    path = "data/player_data/player_data.csv"
    return pd.read_csv(os.path.join(Config.PROJECT_DIR, path))


def prep_players_data():
    players = import_players()[['tag', 'name', 'role']]
    return players


def upsert_players():
    players = prep_players_data().set_index('tag')
    engine = get_engine()
    result = pangres.upsert(con=engine, df=players, table_name='players',
                            if_row_exists='update', create_schema=False,
                            create_table=False, add_new_columns=False,
                            dtype={'tag': String(10)}, yield_chunks=True)
    for chunk in result:
        print(f'players -- {chunk.rowcount} row(s) updated')


def prep_player_status_logs_data():
    columns = ['tag', 'expLevel', 'townHallLevel']
    player_status_logs = import_players()[columns]
    rename_dict = {'tag': 'player_tag',
                   'expLevel': 'exp_level',
                   'townHallLevel': 'town_hall_level'}
    player_status_logs = player_status_logs.rename(columns=rename_dict)
    return player_status_logs


def insert_player_status_logs():
    player_status_logs = prep_player_status_logs_data()
    player_status_logs.to_sql('player_status_logs', get_engine(), if_exists='append', index=False)
    print(f'player_status_logs -- {len(player_status_logs)} row(s) inserted')


def prep_player_activity_logs_data():
    columns = ['tag', 'league', 'trophies', 'attackWins', 'donations', 'donationsReceived']
    player_activity_logs = import_players()[columns]
    rename_dict = {'tag': 'player_tag',
                   'attackWins': 'attack_wins',
                   'donations': 'donations_sent',
                   'donationsReceived': 'donations_received'}
    player_activity_logs = player_activity_logs.rename(columns=rename_dict)
    player_activity_logs['league'] = player_activity_logs['league'].fillna("{'name': None}")
    player_activity_logs['league'] = player_activity_logs['league'].apply(lambda x: ast.literal_eval(x))
    player_activity_logs['league'] = player_activity_logs['league'].apply(lambda x: x['name'])
    return player_activity_logs


def insert_player_activity_logs():
    player_activity_logs = prep_player_activity_logs_data()
    player_activity_logs.to_sql('player_activity_logs', get_engine(), if_exists='append', index=False)
    print(f'player_activity_logs -- {len(player_activity_logs)} row(s) inserted')


if __name__ == '__main__':
    upsert_players()
    insert_player_status_logs()
    insert_player_activity_logs()
