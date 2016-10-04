from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def daddies(request):
    #Endpoint in Services container to return all daddies
    url = 'http://sugar_services:8000/api/v1/services/daddies'
    #Make GET request
    daddies_json = requests.get(url)
    #Make template context
    context = {'daddies': daddies_json.content}
    #Render template
    return render(request, 'daddies.html', context)

def babies(request):
    #Endpoint in Services container to return all daddies
    url = 'http://sugar_services:8000/api/v1/services/babies'
    #Make GET request
    babies_json = requests.get(url)
    #Make template context
    context = {'babies': babies_json.content}
    #Render template
    return render(request, 'babies.html', context)

def search(request):
    return render(request, 'search.html')
