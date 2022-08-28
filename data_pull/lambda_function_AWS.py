import boto3
from datetime import datetime, timezone
import json
from os import listdir, path
import pandas as pd
import urllib3

S3_CLIENT = boto3.client("s3")
S3_BUCKET = "clan-data-storage"
LOCAL_FILE_SYS = "/tmp"
HEADERS = {
    'Accept':'application/json',
    'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjUwOWFiNjIyLTEwZDAtNGY5OC1hODc2LWMxYzEzMzY5NmU3MCIsImlhdCI6MTYzNTYyOTk5OSwic3ViIjoiZGV2ZWxvcGVyL2RlMTE5MTZkLWI4ZDktNjcwYi04MmZlLTdjOGRjYzQ4MjE3NiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4LjExOS43NC4yMDAiXSwidHlwZSI6ImNsaWVudCJ9XX0.aQtk4fDS8IvgBsnkzKZrZ2G31cjZcJToZeMQbUhXMOXKdQRIlWUCQ1hhWpoSoWtmUWppLEynnJnkIR7Z7FLpZw'
}

def _get_key():
    dt_now = datetime.now(tz=timezone.utc)
    KEY = (
        dt_now.strftime("%Y-%m-%d")
        + "/"
        + dt_now.strftime("%H")
        + "/"
        + dt_now.strftime("%M")
        + "/"
    )
    return KEY

def get_data(clan_id='YQLJ9CRU', headers=HEADERS):
    http = urllib3.PoolManager(headers=headers)
    response = http.request("GET", 
        'https://api.clashofclans.com/v1/clans/%23{}/members'.format(clan_id),
        retries=urllib3.util.Retry(3))
    data = json.loads(response.data.decode("utf8").replace("'", '"'))['items']
    return data

def parse_data(data):
    df = pd.DataFrame(data)
    return df

def write_to_local(df, part, loc=LOCAL_FILE_SYS):
    file_name = loc + "/" + str(part) + '.csv'
    df.to_csv(file_name, index=False)
    return file_name

def download_data(N=1):
    for i in range(0, N):
        data = get_data()
        df = parse_data(data)
        write_to_local(df, i)

def lambda_handler(event, context):
    download_data()
    key = _get_key()
    files = [f for f in listdir(LOCAL_FILE_SYS) if path.isfile(path.join(LOCAL_FILE_SYS, f))]
    for f in files:
        S3_CLIENT.upload_file(LOCAL_FILE_SYS + "/" + f, S3_BUCKET, key + f)