from django.shortcuts import render
from rest_framework import generics
from .serializers import NoutDeteilSerializer, NoutListlSerializer
from .models import Noutbuk
from .serializers import NoutDeteilSerializer

class NoutCreateView(generics.CreateAPIView):
    serializer_class = NoutDeteilSerializer



class NoutListVIiew(generics.ListAPIView):
    serializer_class = NoutListlSerializer
    queryset = Noutbuk.objects.all()



class NoutDeteilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoutDeteilSerializer
    queryset = Noutbuk.objects.all()


