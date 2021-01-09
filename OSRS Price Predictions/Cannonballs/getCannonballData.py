from bs4 import BeautifulSoup as bs
import requests
import time
import csv

items = ['Cannonball', 'Steel_bar', 'Iron_ore', 'Coal']

baseUrl = 'https://oldschool.runescape.wiki/w/Module:Exchange/'

for item in items:
    dataRows = []

    print('Getting data for item: ' + item)

    url = baseUrl + item + '/Data'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')

    dataPoints = soup.select('span:nth-of-type(n+4)')
    print(dataPoints)

    for dataPoint in dataPoints:
        data = dataPoint.text

        dataRows.append(data)





    #write to file
    with open(item + ".csv", 'w') as out_f:
        for row in dataRows:
            out_f.write(row)