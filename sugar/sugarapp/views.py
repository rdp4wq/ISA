from django.shortcuts import render
from rest_framework import generics
from sugarapp.models import Baby, Daddy
from sugarapp.serializers import BabySerializer, DaddySerializer


class BabyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

class BabyList(generics.ListCreateAPIView):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    def list(self, request, *args, **kwargs):
        response = super(BabyList, self).list(request, *args, **kwargs) # call the original 'list'
        response.data = {"babbies": response.data} # customize the response data
        return response # return response with this custom representation

class DaddyDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Daddy.objects.all()
    serializer_class = DaddySerializer

class DaddyList(generics.ListCreateAPIView):
    queryset = Daddy.objects.all()
    serializer_class = DaddySerializer

    def list(self, request, *args, **kwargs):
        response = super(DaddyList, self).list(request, *args, **kwargs) # call the original 'list'
        response.data = {"daddies": response.data} # customize the response data
        return response # return response with this custom representation

def index(request):
    return render(request, 'babies/index.html')