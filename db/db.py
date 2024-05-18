import pymongo
import logging
import os
import urllib.parse

# Instead of dotenv, using os.environ to fetch environment variables
class DBconnect:
    def __init__(self, collection):
        self.database = os.environ.get("MONGO_DB")
        self.collection = collection
        self.logger = logging.getLogger(__name__)

    def connect(self):
        username = urllib.parse.quote_plus("admin")
        password = urllib.parse.quote_plus("poiuytrewq")
        port = os.environ.get("MONGO_PORT", "27017")
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
