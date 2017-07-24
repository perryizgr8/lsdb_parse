import json

file = open('lsdb.json')
lsdb = json.load(file)

i = 0
for lsa in lsdb:
    print(lsdb[lsa]['advert'])
    i = i + 1
print(i)