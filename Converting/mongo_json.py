import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
import json

dbku = x['marvel']
col = dbku['avengers']
all_data = list(col.find())

keyy = []
for item in all_data:
    for key in item.keys():
        keyy.append(key)
keyx = list(sorted(set(keyy)))

datajson = []
for item in all_data:
    temp = {}
    for key,val in item.items():
        if key == '_id':
            temp[key] = str(val)
        else:    
            temp[key] = val
    datajson.append(temp)

with open ('mongo2json.json','w') as x:
    json.dump(datajson, x)