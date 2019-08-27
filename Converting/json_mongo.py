import json
import pymongo

with open ('csv2json.json') as x:
    data = json.load(x)

y = pymongo.MongoClient('mongodb://localhost:27017')

db = y['toko_online']
col = db['users3']

for item in data:
    col.insert_one(item)