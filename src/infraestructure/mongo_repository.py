from pymongo import MongoClient
from constants.constants import *

class MongoRepository():
    def __init__(self):
        self.client: MongoClient = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]

    def close_connection(self)-> None:
        self.client.close()