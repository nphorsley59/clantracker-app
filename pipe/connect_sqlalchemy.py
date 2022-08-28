from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from config import Config


def get_engine(url):
    if not database_exists(url):
        create_database(url)
    psql_engine = create_engine(url, pool_size=50, echo=False)
    return psql_engine


def get_session():
    url = Config.DB_URL
    engine = get_engine(url)
    session = sessionmaker(bind=engine)()
    return session


if __name__ == '__main__':
    print(get_session())
