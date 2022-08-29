import os
import pandas as pd
from config import Config
from pipe.connect_sqlalchemy import get_engine
from sqlalchemy import String
import pangres
import ast


def import_players():
    path = "data/player_data/player_data.csv"
    return pd.read_csv(os.path.join(Config.PROJECT_DIR, path))


def prep_players_data():
    players = import_players()[['tag', 'name', 'role']]
    return players


def upsert_players_table():
    players = prep_players_data().set_index('tag')
    engine = get_engine()
    result = pangres.upsert(con=engine, df=players, table_name='players',
                            if_row_exists='update', create_schema=False,
                            create_table=False, add_new_columns=False,
                            dtype={'tag': String(10)}, yield_chunks=True)
    for chunk in result:
        print(f'{chunk.rowcount} row(s) updated')


def prep_player_logs_data():
    player_logs_columns = ['tag', 'expLevel', 'townHallLevel', 'league', 'trophies',
                           'attackWins', 'donations', 'donationsReceived']
    player_logs = import_players()[player_logs_columns]
    player_logs_column_rename_dict = {'expLevel': 'exp_level',
                                      'townHallLevel': 'town_hall_level',
                                      'attackWins': 'attack_wins',
                                      'donations': 'donations_sent',
                                      'donationsReceived': 'donations_received'}
    player_logs = player_logs.rename(columns=player_logs_column_rename_dict)
    player_logs['league'] = player_logs['league'].apply(lambda x: ast.literal_eval(x))
    player_logs['league'] = player_logs['league'].apply(lambda x: x['name'])
    return player_logs


def insert_player_logs_table():
    player_logs = prep_player_logs_data()
    player_logs.to_sql('player_logs', get_engine(), if_exists='append', index=False)


if __name__ == '__main__':
    upsert_players_table()
    insert_player_logs_table()
