import pymongo
import json
from bson import json_util
class DBClient(object):
    
    #creates a collection for scouting data 
    def __init__(self, ip, port):

        self.client = pymongo.MongoClient(ip, port)
        self.db = self.client['victiScout']
        self.collection = self.db['scoutData']
        self.data = []

    def insertData(self, j):
        #inserts into the collection (table)
        self.collection.insert(j)

    def getAllResults(self):
        
        #gets all scouting data in a cursor
        cursor = self.collection.find()
        
        #converts cursor to json 
        for doc in cursor:
            tmp_doc = json.dumps(doc, default=json_util.default)
            self.data.append(tmp_doc)
        return str(self.data)     
        
