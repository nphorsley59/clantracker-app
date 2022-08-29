import os
import pandas as pd
from config import Config
from pipe.connect_sqlalchemy import get_engine
from sqlalchemy import String
import pangres


def import_players():
    path = "data/player_data/player_data.csv"
    return pd.read_csv(os.path.join(Config.PROJECT_DIR, path))


def process_players():
    players = import_players()[['tag', 'name', 'role']]
    return players


def upsert_players_table():
    players = process_players().set_index('tag')
    engine = get_engine(url=Config.DB_URL)
    result = pangres.upsert(con=engine, df=players, table_name='players',
                            if_row_exists='update', create_schema=False,
                            create_table=False, add_new_columns=False,
                            dtype={'tag': String(10)}, yield_chunks=True)
    for chunk in result:
        print(f'{chunk.rowcount} row(s) updated')


if __name__ == '__main__':
    print(upsert_players_table())
