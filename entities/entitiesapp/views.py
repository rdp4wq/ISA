from rest_framework import generics, viewsets
from entitiesapp.serializers import UserSerializer, AuthenticatorSerializer, DateSerializer
from entitiesapp.models import User, Authenticator, Date
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt


class EntitiesViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        response = super(EntitiesViewSet, self).list(request, *args, **kwargs)
        response.data = {'users': response.data}
        return response

class UserViewSet(EntitiesViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthentiactorViewSet(EntitiesViewSet):
    queryset = Authenticator.objects.all()
    serializer_class = AuthenticatorSerializer

class DateViewSet(EntitiesViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

@csrf_exempt
@require_POST
def login(request):
    try:
        user = User.objects.filter(username=request.POST['username'], password=request.POST['password']).get()
    except ObjectDoesNotExist:
        raise Http404('Invalid login')
    auth = Authenticator.create_authenticator(user)
    auth.save()
    return JsonResponse({'authenticator': auth.authenticator})
