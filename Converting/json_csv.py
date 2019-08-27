import json
import csv

with open ('csv2json.json') as x:
    data = json.load(x)

keyy = []
for item in data:
    for key in item.keys():
        keyy.append(key)
keyx = list(sorted(set(keyy)))

with open ('json.csv','w',newline='') as x:
    writer = csv.DictWriter(x, fieldnames=keyx)
    writer.writeheader()
    writer.writerows(data)