import csv
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    # port = 3306,
    user = 'root',
    password = '######',
    database = 'coba000'
)
kursor = db.cursor()

all_data = []
with open ('sql2csv.csv','r',newline='') as x:
    reader = csv.DictReader(x)
    for item in reader:
        all_data.append(dict(item))

keyx = []
for key in all_data[0].keys():
    keyx.append(key)

kursor.execute('create table coba_123 ({} varchar(100))'.format(keyx[0]))

for loop in range (len(keyx)-1):
    kursor.execute('''alter table coba_123
add column 
{} varchar(100)'''.format(keyx[loop+1]))
    db.commit()

keyx = []
valx = []
for item in all_data:
    k = []
    v = []
    for key,val in item.items():
        k.append(key)
        v.append(val)
    keyx.append(k)
    valx.append(v)

for key,val in zip(keyx,valx):
    kursor.execute('insert into coba_123 {} values {}'.format(str(tuple(key)).replace("'",''),str(tuple(val)).replace("{'",'').replace("'}",'')))
    db.commit()