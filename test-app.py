
import requests
from requests.api import head
import csv


url = "http://api.nbp.pl/api/cenyzlota/last/30/?format=json"


headers={
    'Accept': 'application/json',
    'Content-type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()

convertedData= []
csvHeader=['DATA','CENA']

for x in myjson:
    listing=[x['data'],x['cena']]
    convertedData.append(listing)

with open('test.csv','w',encoding='UTF8', newline='') as f:
    writer =csv.writer(f)

    writer.writerow(csvHeader)
    writer.writerows(convertedData)

    print('done')

