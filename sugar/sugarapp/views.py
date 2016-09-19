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

class DaddyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Daddy.objects.all()
    serializer_class = DaddySerializer

class DaddyList(generics.ListCreateAPIView):
    queryset = Daddy.objects.all()
    serializer_class = DaddySerializer

def index(request):
    return render(request, 'babies/index.html')