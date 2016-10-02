from django.shortcuts import render
from django.http import JsonResponse
import requests

def get_daddies_from_models(request):
    #Call daddies endpoint in Model container
    url = 'http://192.168.99.100:8001/api/v1/daddies/'
    #Make GET
    r = requests.get(url)
    #Format response as json
    daddies_json = r.json()
    #Return json response
    return JsonResponse(daddies_json, content_type='application/json')
