from rest_framework import generics, viewsets, decorators
from rest_framework.response import Response
from entitiesapp.serializers import UserSerializer, AuthenticatorSerializer, DateSerializer
from entitiesapp.models import User, Authenticator, Date
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt


class EntitiesViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        response = super(EntitiesViewSet, self).list(request, *args, **kwargs)
        response.data = {'result': response.data}
        return response


class UserViewSet(EntitiesViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserByUsernameViewSet(EntitiesViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class AuthenticatorViewSet(EntitiesViewSet):
    queryset = Authenticator.objects.all()
    serializer_class = AuthenticatorSerializer


class AuthenticatorByUserViewSet(EntitiesViewSet):
    queryset = Authenticator.objects.all()
    serializer_class = AuthenticatorSerializer
    lookup_field = 'user'


class DateViewSet(EntitiesViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
