from django.shortcuts import render
from django.http import JsonResponse, Http404
import requests
from services.settings import ENTITIES_URL


def get_users_from_models(request):
    # Call users endpoint in Model container
    # url = 'http://sugar_entities:8000/api/v1/users/'
    url = ENTITIES_URL + 'api/v1/users/'
    # Make GET
    r = requests.get(url)
    # Format response as json
    users_json = r.json()
    # Return json response
    return JsonResponse(users_json, content_type='application/json')


def get_user_from_models(request, pk):
    # Call users endpoint in Model container
    # url = 'http://sugar_entities:8000/api/v1/users/' + pk + '/'
    url = ENTITIES_URL + 'api/v1/users/' + pk + '/'
    # Make GET
    r = requests.get(url)
    # Format response as json
    user_json = r.json()
    # Return json response
    return JsonResponse(user_json, content_type='application/json')


def get_babies_from_models(request):
    # Call users endpoint in Model container
    # url = 'http://sugar_entities:8000/api/v1/users/'
    url = ENTITIES_URL + 'api/v1/users/'
    # Make GET
    r = requests.get(url)
    # Format response as json
    users_json = r.json()
    babies_json = {
        'babies': [user for user in users_json['users'] if user['user_type'] == 'Baby']
    }
    return JsonResponse(babies_json, content_type='application/json')


def get_baby_from_models(request, pk):
    # Call users endpoint in Model container
    url = ENTITIES_URL + 'api/v1/users/' + pk + '/'
    # Make GET
    r = requests.get(url)
    # Format response as json
    baby_json = r.json()
    if baby_json['user_type'] != 'Baby':
        raise Http404('Baby does not exist')
    return JsonResponse(baby_json, content_type='application/json')


def get_daddies_from_models(request):
    # Call users endpoint in Model container
    # url = 'http://sugar_entities:8000/api/v1/users/'
    url = ENTITIES_URL + 'api/v1/users/'
    # Make GET
    r = requests.get(url)
    # Format response as json
    users_json = r.json()
    daddy_json = {
        'daddies': [user for user in users_json['users'] if user['user_type'] == 'Daddy']
    }
    return JsonResponse(daddy_json, content_type='application/json')
