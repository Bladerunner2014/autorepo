import pymongo
import logging
import pymongo.errors
from db.db import DBconnect
import json
from bson import json_util
from typing import List, Dict
from datetime import datetime

logger = logging.getLogger(__name__)
Time_Interval = Dict[str, datetime]
Records = List[Dict]


class Dao:

    def __init__(self, collection):
        self.db = DBconnect(collection).connect()

    def insert_one(self, document: dict):
        try:
            res = self.db.insert_one(document)
        except pymongo.errors as error:
            logger.error(error)
            raise error
        return res

    def find(self, condition: dict):
        try:
            dt = self.parse_json(self.db.find(condition, {'_id': 0}))

            return dt
            # return self.db.find_one(condition)
        except pymongo.errors as error:
            logger.error(error)
            raise error

    def find_one(self, condition: dict):
        try:
            dt = self.parse_json(self.db.find_one(condition, {'_id': 0}))

            return dt
            # return self.db.find_one(condition)
        except pymongo.errors as error:
            logger.error(error)
            raise error

    def update(self, condition: dict, new_values: dict):
        new_values = {"$set": new_values}

        try:
            r = self.db.update_one(condition, new_values)
        except pymongo.errors as error:
            logger.error(error)
            raise error
        return r

    def delete(self, condition: dict):
        try:
            self.db.delete_one(condition)
        except pymongo.errors as error:
            logger.error(error)
            raise error

    @staticmethod
    def parse_json(data):
        return json.loads(json_util.dumps(data))

