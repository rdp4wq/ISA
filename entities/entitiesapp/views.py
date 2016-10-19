from rest_framework import generics
from entitiesapp.serializers import UserSerializer
from entitiesapp.models import User, Authenticator
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        response = super(UserList, self).list(request, *args, **kwargs)  # call the original 'list'
        response.data = {'users': response.data}  # customize the response data
        return response  # return response with this custom representation


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
