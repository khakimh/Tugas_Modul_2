import mysql.connector
import pymongo

db = mysql.connector.connect(
    host = 'localhost',
    # port = 3306,
    user = 'root',
    password = '######',
    # auth_plugin = 'sha256_password',
    database = 'toko_online')
x = pymongo.MongoClient('mongodb://localhost:27017')

kursor = db.cursor()
querydb1 = 'describe users'
kursor.execute(querydb1)
keyx = []
for item in kursor.fetchall():
    keyx.append(item[0])

querydb2 = 'select * from users'
kursor.execute(querydb2)
all_data = kursor.fetchall()
dataCsv = []

for item in all_data:
    temp = {}
    for loop in range (len(item)):
        if type(item[loop]) == type({'a'}):
            temp[keyx[loop]] = str(item[loop])[2:-2]
        else:
            temp[keyx[loop]] = item[loop]
    dataCsv.append(temp)

db = x['toko_online']
col = db['users']

for item in dataCsv:
    col.insert_one(item)