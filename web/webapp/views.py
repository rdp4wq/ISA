import json

import requests
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from web.settings import SERVICES_URL
from webapp.forms import LoginForm, RegisterForm, DateForm


# Create your views here.
def index(request):
    # request.session.set_test_cookie()
    auth = request.COOKIES.get('auth')
    is_logged_in = False
    if auth:
        is_logged_in = True
    context = {'is_logged_in': is_logged_in}

    return render(request, 'index.html', context)


# def daddies(request):
#     # Endpoint in Services container to return all daddies
#     url = SERVICES_URL + 'api/v1/services/daddies'
#     # Make GET request
#     daddies_json = requests.get(url)
#     # Make template context
#     context = {'daddies': daddies_json.content}
#     # Render template
#     return render(request, 'daddies.html', context)


def babies(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect("/login/")

    # Endpoint in Services container to return all daddies
    url = SERVICES_URL + 'api/v1/services/babies'
    # Make GET request
    babies_json = requests.get(url)
    # Make template context
    context = {'babies': babies_json.content}
    # Render template
    return render(request, 'babies.html', context)


# def baby_detail(request, baby_id):
#     # Endpoint in Services container to return a single baby
#     url = SERVICES_URL + 'api/v1/services/babies/' + baby_id + '/'
#     # Make GET request
#     baby_json = requests.get(url)
#     # Convert json into dict, make template context
#     baby = baby_json.content.decode()
#     context = json.loads(baby)
#     # Render template
#     return render(request, 'baby.html', context)


def search(request):
    return render(request, 'search.html')


@csrf_exempt
# @require_POST
def login(request):
    auth = request.COOKIES.get('auth')
    if auth:
        return HttpResponseRedirect("/")

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

            response = HttpResponseRedirect("/")

            try:
                jsonresponse = str(r.content, encoding='utf8')
                final_json = json.loads(jsonresponse)

                #save stuff from services in cookie
                response.set_cookie("auth", final_json['authenticator'])
                response.set_cookie("user", final_json['user'])
            except ValueError:  # includes simplejson.decoder.JSONDecodeError
                return render(request, 'login.html', {'form': form, 'error': "Invalid login"})

            return response
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error': "", 'is_logged_in': False})


@csrf_exempt
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = request.POST.copy()
            if data['income'] == '':
                data['income'] = None


            #####
            #This endpoint should take in form-data with the fields 'username' and 'password'
            #####
            url = SERVICES_URL + 'api/v1/register/'

            #pass form data to services
            requests.post(url, data)

            return HttpResponse(r.content)
            response = HttpResponseRedirect("/")
            return response
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, 'is_logged_in': False})


def logout(request):

    response = HttpResponseRedirect("/")
    response.delete_cookie("auth")

    return response


# @csrf_exempt
# def create_date(request):
#     auth = request.COOKIES.get('auth')
#     if not auth:
#         return HttpResponseRedirect("/login")
#
#     if request.method == 'POST':
#         form = DateForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             data = request.POST.copy()
#             data['user'] = 3
#
#             #####
#             #This endpoint should take in form-data with the fields 'username' and 'password'
#             #####
#             url = SERVICES_URL + 'api/v1/dates/new/'
#
#             #pass form data to services
#
#
#             r = requests.post(url, data)
#
#             #get back stuff from services
#             return HttpResponse(r.content)
#             response = HttpResponseRedirect("/")
#
#             return response
#     else:
#         form = DateForm()
#         return render(request, 'create.html', {'form': form, 'is_logged_in': True})

@csrf_exempt
def create_date(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect("/login")
    if request.method == 'POST':

        form = DateForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            data = request.POST.copy()
            data['user'] = 10


            #####
            #This endpoint should take in form-data with the fields 'username' and 'password'
            #####
            url = SERVICES_URL + 'api/v1/dates/new/'

            #pass form data to services
            r = requests.post(url, request.POST)

            return HttpResponse(r.content)
            # response = HttpResponseRedirect("/")
            # return response
        else:
            return HttpResponse(form)
    else:
        form = DateForm()

    return render(request, 'create.html', {'form': form, 'is_logged_in': True})