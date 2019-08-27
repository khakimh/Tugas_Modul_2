import csv
import pymongo

y = pymongo.MongoClient('mongodb://localhost:27017')

all_data = []
with open ('sql2csv.csv','r',newline='') as x:
    reader = csv.DictReader(x)
    for item in reader:
        all_data.append(dict(item))

db = y['toko_online']
col = db['users2']

for item in all_data:
    col.insert_one(item)