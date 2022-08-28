from dotenv import load_dotenv
import os
import pandas as pd


pd.options.display.max_columns = None
pd.options.display.max_rows = 300
pd.set_option('display.width', 500)


class Config:
    PROJECT_DIR = os.path.dirname(__file__)
    if os.path.isfile(os.path.join(PROJECT_DIR, 'local.env')):
        load_dotenv(os.path.join(PROJECT_DIR, 'local.env'))
    CLASH_API_KEY = os.environ.get("CLASH_API_KEY", "")
    DB_USER = os.environ.get("DB_USER", "")
    DB_PASS = os.environ.get("DB_PASS", "")
    DB_HOST = os.environ.get("DB_HOST", "")
    DB_PORT = os.environ.get("DB_PORT", "")
    DB_NAME = os.environ.get("DB_NAME", "")
    DB_URL = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


if __name__ == '__main__':
    print(Config.CLASH_API_KEY)
