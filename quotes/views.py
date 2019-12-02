from django.shortcuts import render
from .models import Stock


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        # pk_24309d8520344e4da571858c2dec509b
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_24309d8520344e4da571858c2dec509b")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above.."})

    

def about(request):
    return render(request, 'about.html', {})


def add_stock(request):

    ticker = Stock.objects.all()
    return render(request, 'add_stock.html', {'ticker': ticker})


