import pymongo
import json
from bson import json_util

class DBClient(object):

    # Create a collection to hold scouting data
    def __init__(self, ip, port):

        self.client = pymongo.MongoClient(ip, port)
        self.db = self.client['victiScout']
        self.collection = self.db['scoutData']
        self.data = []

    def insertData(self, j):

        # Insert data into the collection
        self.collection.insert(j)

    def getData(self):

        # Get all the data
        cursor = self.collection.find()

        # Convert to JSON
        for doc in cursor:
            tmp_doc = json.dumps(doc, default = json_util.default)
            self.data.append(tmp_doc)
        return str(self.data)