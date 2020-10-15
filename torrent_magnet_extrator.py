import requests
import json

query=input("enter the item you are looking for :")
api_url='https://api.sumanjay.cf/torrent/?query='
final_url=api_url+str(query)
r=requests.get(final_url)
data=r.json()
for i in range(len(data)):
    if(data[i]['seeder']>10):
        print(data[i]['magnet'])
    else:
        print("sorry, there is no toorent available with more than 10 seeders")
        break