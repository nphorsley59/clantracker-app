# import libraries
import pandas as pd
import sqlalchemy

# connect to mysql
engine = sqlalchemy.create_engine('mysql+pymysql://root:Goliath59nph!!@localhost:3306/clashdb')
df = pd.read_sql_table("activity", engine)
