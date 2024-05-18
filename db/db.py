import pymongo
import logging
from dotenv import dotenv_values
import urllib.parse

config = dotenv_values(".env")


class DBconnect:
    def __init__(self, collection):
        self.database = config["MONGO_DB"]
        self.collection = collection
        self.logger = logging.getLogger(__name__)

    def connect(self):
        username = urllib.parse.quote_plus("admin")
        password = urllib.parse.quote_plus("poiuytrewq")
        port = config["MONGO_PORT"]
        try:
            client = pymongo.MongoClient(f"mongodb://{username}:{password}@mongodb:{port}/?authSource=admin")
            self.logger.info("Successfully connected to MongoDB")
        except pymongo.errors.OperationFailure as error:
            self.logger.error(f"Authentication failed: {error}")
            raise
        except Exception as error:
            self.logger.error(f"Connection error: {error}")
            raise

        try:
            database = client[self.database]
            collection = database[self.collection]
        except Exception as error:
            self.logger.error(f"Database/Collection error: {error}")
            raise

        return collection
