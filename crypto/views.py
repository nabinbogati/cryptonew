from django.shortcuts import render
import requests
import json

def home(request):

    # Grab Crypto Price Data
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,LTC,XLM,ADA,USDT,MIOTA,&tsyms=USD')
    price = json.loads(price_request.content)

    # Grab Crypto Data
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):

    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+',&tsyms=USD')
        crypto = json.loads(crypto_request.content)
        return render(request,'prices.html',{'quote':quote, 'crypto': crypto})
    else:
        notfound = "OOPS!!!Enter a Currency Symbol in From Below"
        return render(request,'prices.html',{'notfound':notfound})
