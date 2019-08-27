import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
import csv

dbku = x['marvel']
col = dbku['avengers']
all_data = list(col.find())

keyy = []
for item in all_data:
    for key in item.keys():
        keyy.append(key)
keyx = list(sorted(set(keyy)))

dataCsv = []
for item in all_data:
    temp = {}
    for key,val in item.items():
        if key == '_id':
            temp[key] = str(val)
        else:    
            temp[key] = val
    dataCsv.append(temp)

    with open ('mongodb.csv','w',newline='') as x:
        writer = csv.DictWriter(x, fieldnames=keyx)
        writer.writeheader()
        writer.writerows(dataCsv)