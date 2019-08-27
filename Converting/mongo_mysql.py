import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
import mysql.connector
db = mysql.connector.connect(
    host = 'localhost',
    # port = 3306,
    user = 'root',
    password = '######',
    auth_plugin = 'sha256_password',
    database = 'toko_online'
)
kursor = db.cursor()

dbku = x['marvel']
col = dbku['avengers']
all_data = list(col.find())

keyy = []
for item in all_data:
    for key in item.keys():
        keyy.append(key)
keyx = list(sorted(set(keyy)))

kursor.execute('create table mongo_2_mysql ({} varchar(100))'.format(keyx[0]))

for loop in range (len(keyx)-1):
    kursor.execute('''alter table mongo_2_mysql
add column 
{} varchar(100)'''.format(keyx[loop+1]))
    db.commit()

keyz = []
valz = []
for item in all_data:
    k = []
    v = []
    for key,val in item.items():
        k.append(key)
        v.append(val)
    keyz.append(k)
    valz.append(v)

for key,val in zip(keyz,valz):
    kursor.execute('insert into mongo_2_mysql ({}) values ({})'.format(str(key)[1:-1].replace("'",''),str(val)[9:-1].replace("(",'').replace(")",'')))
    db.commit()