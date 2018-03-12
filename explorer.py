import requests
import json
import time 
from prettytable import PrettyTable


while True:
    # base URLs
    globalURL = "https://api.coinmarketcap.com/v1/global/"
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

    t = PrettyTable(['Name', 'Ticker','Price in USD', 'Rank', 'Percentage change 1hr', 'Percentage change 24 hr', 'Percentage change 7days', 'Last updated'])

    # get data from globalURL
    request = requests.get(globalURL)
    data = request.json()

    # menu
    print()
    print("Welcome to the Cryptocurrency Explorer!")
    print("Enter 'all' or 'name of crypto' (i.e. bitcoin) to see the name of the top 100 currencies or a specific currency")
    print()
    coin = input("Enter the Cryptocurrency: ")

    if coin == "all":
        request = requests.get(tickerURL)
        data = request.json()

        for x in data:
            ticker = x['symbol']
            name = x['name']
            price = x['price_usd']
            rank = x['rank']
            percent_change_1hr = x['percent_change_1h']
            percent_change_24hr = x['percent_change_24h']
            percent_change_7d = x['percent_change_7d']
            epoch = int(x['last_updated'])
            last_updated = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))

            t.add_row([name,ticker,price,rank,percent_change_1hr,percent_change_24hr,percent_change_7d, last_updated])
            
            
        print(t)

    else:
        tickerURL += '/'+coin+'/'
        request = requests.get(tickerURL)
        data = request.json()

        name = data[0]['name']
        ticker = data[0]['symbol']
        price = data[0]['price_usd']
        rank = data[0]['rank']
        percent_change_1hr = data[0]['percent_change_1h']
        percent_change_24hr = data[0]['percent_change_24h']
        percent_change_7d = data[0]['percent_change_7d']
        epoch = int(data[0]['last_updated'])
        last_updated = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))

        
        
        t.add_row([name,ticker,price,rank,percent_change_1hr,percent_change_24hr,percent_change_7d, last_updated])
        print(t)
        

    coin2 = input("Another coin (y/n): ")
    if coin2 == "y":
        continue
    if coin2 == "n":
        break