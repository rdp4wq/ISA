from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    return render(request, 'index.html')

def daddies(request):
    url = 'http://192.168.99.100:8001/api/v1/daddies/'
    r = requests.get(url)
    daddies_json = r.json()
    daddies_list= {'books':daddies_json['daddies']}
    context = {'daddies': daddies_list}

    return render(request, 'daddies.html', context)