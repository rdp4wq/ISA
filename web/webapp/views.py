from django.shortcuts import render
import requests
import json
from web.settings import SERVICES_URL

# Create your views here.
def index(request):
    return render(request, 'index.html')


def daddies(request):
    # Endpoint in Services container to return all daddies
    url = SERVICES_URL + 'api/v1/services/daddies'
    # Make GET request
    daddies_json = requests.get(url)
    # Make template context
    context = {'daddies': daddies_json.content}
    # Render template
    return render(request, 'daddies.html', context)


def babies(request):
    # Endpoint in Services container to return all daddies
    url = SERVICES_URL + 'api/v1/services/babies'
    # Make GET request
    babies_json = requests.get(url)
    # Make template context
    context = {'babies': babies_json.content}
    # Render template
    return render(request, 'babies.html', context)


def baby_detail(request, baby_id):
    # Endpoint in Services container to return a single baby
    url = SERVICES_URL + 'api/v1/services/babies/' + baby_id + '/'
    # Make GET request
    baby_json = requests.get(url)
    # Convert json into dict, make template context
    baby = baby_json.content.decode()
    context = json.loads(baby)
    # Render template
    return render(request, 'baby.html', context)


def search(request):
    return render(request, 'search.html')
