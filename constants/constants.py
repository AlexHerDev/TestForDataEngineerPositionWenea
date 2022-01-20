import os

MONGO_URI: str = f"mongodb://{os.environ['MONGO_ROOT_USERNAME']}:{os.environ['MONGO_ROOT_PASSWORD']}@{os.environ['DATABASE_ADDRESS']}:{os.environ['DATABASE_PORT']}/"
DB_NAME: str = os.environ["DATABASE_NAME"]
MAX_BYTES_TO_PERSIST: int = int(os.environ["MAX_BYTES_TO_PERSIST"])
DATA_URL: str = f"https://raw.githubusercontent.com/chargeprice/open-ev-data/master/data/ev-data.json"
DATA_URL_2: str = f"https://data.wa.gov/api/views/f6w7-q2d2/rows.json"
