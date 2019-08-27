import json
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    # port = 3306,
    user = 'root',
    password = '######',
    # auth_plugin = 'sha256_password',
    database = 'toko_online')

with open ('csv2json.json') as x:
    data = json.load(x)
    kursor = db.cursor()


keyy = []
for item in data:
    for key in item.keys():
        keyy.append(key)
keyx = list(sorted(set(keyy)))

kursor.execute('create table json ({} varchar(100))'.format(keyx[0]))

for loop in range (len(keyx)-1):
    kursor.execute('''alter table json
add column 
{} varchar(100)'''.format(keyx[loop+1]))
    db.commit()

keyx = []
valx = []
for item in data:
    k = []
    v = []
    for key,val in item.items():
        k.append(key)
        v.append(val)
    keyx.append(k)
    valx.append(v)
    
for key,val in zip(keyx,valx):
    kursor.execute('insert into json {} values {}'.format(str(tuple(key)).replace("'",''),str(tuple(val)).replace("{'",'').replace("'}",'')))
    db.commit()