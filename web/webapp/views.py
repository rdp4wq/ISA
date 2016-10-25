import json

import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from web.settings import SERVICES_URL
from webapp.forms import LoginForm, RegisterForm


# Create your views here.
def index(request):
    # request.session.set_test_cookie()

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
    auth = request.COOKIES.get('auth')
    if not auth:
        print()
    else:
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


# @csrf_exempt
# @require_POST
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            #####
            #This endpoint should take in form-data with the fields 'username' and 'password'
            #####
            url = SERVICES_URL + 'api/v1/login/'

            #pass form data to services
            r = requests.post(url, request.POST)

            #get back stuff from services
            jsonresponse = str(r.content, encoding='utf8')
            final_json = json.loads(jsonresponse)

            #save stuff from services in cookie
            response = render(request, "index.html")
            response.set_cookie("auth", final_json['authenticator'])

            return response
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# @csrf_exempt
# @require_POST
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            #####
            #This endpoint should take in form-data with the fields 'username' and 'password'
            #####
            url = SERVICES_URL + 'api/v1/login/'

            #pass form data to services
            requests.post(url, request.POST)

            response = render(request, "index.html")
            return response
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def logout(request):
    response = render(request, "index.html")
    response.delete_cookie("auth")

    return response