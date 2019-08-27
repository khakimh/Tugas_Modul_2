import mysql.connector
import csv

db = mysql.connector.connect(
    host = 'localhost',
    # port = 3306,
    user = 'root',
    password = '######',
    # auth_plugin = 'sha256_password',
    database = 'toko_online'
)

kursor = db.cursor()
querydb1 = 'describe users'
kursor.execute(querydb1)
print(kursor.fetchall())
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
        temp[keyx[loop]] = item[loop]
    dataCsv.append(temp)

with open ('mysql2csv.csv','w',newline='') as x:
    writer = csv.DictWriter(x, fieldnames=dataCsv[0].keys())
    writer.writeheader()
    writer.writerows(dataCsv)