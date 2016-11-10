import json

import requests
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from web.settings import SERVICES_URL
from webapp.forms import LoginForm, RegisterForm, DateForm, SearchForm


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


# def babies(request):
#     auth = request.COOKIES.get('auth')
#     if not auth:
#         return HttpResponseRedirect("/login/")
#
#     # Endpoint in Services container to return all daddies
#     url = SERVICES_URL + 'api/v1/services/babies'
#     # Make GET request
#     babies_json = requests.get(url)
#     # Make template context
#     context = {'babies': babies_json.content}
#     # Render template
#     return render(request, 'babies.html', context)



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


def dates(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect("/login/")
    authenticated = authenticate(request)
    if authenticated == True:
        # Endpoint in Services container to return all daddies
        url = SERVICES_URL + 'api/v1/dates/'


        # Make GET request
        dates_json = requests.get(url)
        decoded_dates = dates_json.content.decode()
        dates = json.loads(decoded_dates)
        # Make template context
        context = {'results': dates['result'], 'is_logged_in': True}
        # Render template
        return render(request, 'dates.html', context)
    else:
        return HttpResponseRedirect("/login/")


def search(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect("/login")
    authenticated = authenticate(request)
    if authenticated == True:
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                url = SERVICES_URL + 'api/v1/search/?search=' + request.POST.get('search')
                r = requests.post(url)

                jsonresponse = r.content.decode('utf8')
                final_json = json.loads(jsonresponse)
                context = {'form': form, 'results': final_json['result'], 'is_logged_in': True}
                return render(request, 'search.html', context)

        else:
            form = SearchForm()

        return render(request, 'search.html', {'form': form, 'error': "", 'is_logged_in': True})
    else:
            return HttpResponseRedirect("/login/")

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
            user_exists = check_if_user_exists(request)

            if user_exists == False:

                #####
                #This endpoint should take in form-data with the fields 'username' and 'password'
                #####
                url = SERVICES_URL + 'api/v1/register/'

                #pass form data to services
                requests.post(url, data)

                response = HttpResponseRedirect("/")
                return response
            else:
                return render(request, 'register.html', {'form': form, 'is_logged_in': False, 'error': 'This username or email is already used'})

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, 'is_logged_in': False, 'error': ""})


def logout(request):

    response = HttpResponseRedirect("/")
    response.delete_cookie("auth")

    return response


@csrf_exempt
def create_date(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect("/login")

    authenticated = authenticate(request)
    if authenticated == True:
        if request.method == 'POST':

            form = DateForm(request.POST)
            # check whether it's valid:

            if form.is_valid():
                data = request.POST.copy()
                data['user'] = request.COOKIES.get('user')


                #####
                #This endpoint should take in form-data with the fields 'username' and 'password'
                #####
                url = SERVICES_URL + 'api/v1/dates/new/'

                #pass form data to services
                requests.post(url, data)

                # return HttpResponse(r.content)
                response = HttpResponseRedirect("/")
                return response
            else:
                return HttpResponse(form)
        else:
            form = DateForm()

        return render(request, 'create.html', {'form': form, 'is_logged_in': True})
    else:
        return HttpResponseRedirect("/login/")


@csrf_exempt
def authenticate(request):
    data = request.POST.copy()
    data['authenticator'] = request.COOKIES.get('auth')

    url = SERVICES_URL + 'api/v1/authenticate/'

    #pass form data to services
    r = requests.post(url, data)
    body_data = json.loads(r.content.decode('utf8'))
    return body_data['result']

@csrf_exempt
def check_if_user_exists(request):
    url = SERVICES_URL + 'api/v1/services/users/'
    data = request.POST.copy()
    username = data['username']
    email = data['email']

    r = requests.post(url, data)

    body_data = json.loads(r.content.decode('utf8'))
    user_exists = False
    for user in body_data['result']:
        if user['username'] == username:
            user_exists = True
        if user['email'] == email:
            user_exists = True
    return HttpResponse(user_exists)



    # return HttpResponse(data['email'])
    # check_url = SERVICES_URL + 'api/v1/'
