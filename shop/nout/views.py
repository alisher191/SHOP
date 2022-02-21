from django.shortcuts import render
from rest_framework import generics
from .serializers import NoutDeteilSerializer, NoutListlSerializer
from .models import Noutbuk
from .serializers import NoutDeteilSerializer, NoutSerializers
from nout.permission import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class NoutViewSet(ModelViewSet):
    queryset = Noutbuk.objects.all()
    serializer_classes = NoutSerializers
    filter_backend = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name']
    search_fields = ['brand', 'NOUT_TYPE']
    ordering_fields = ['name', 'brand']
    


class NoutCreateView(generics.CreateAPIView):
    serializer_class = NoutDeteilSerializer



class NoutListVIiew(generics.ListAPIView):
    serializer_class = NoutListlSerializer
    queryset = Noutbuk.objects.all()
    permission_classes = (IsAuthenticated, )



class NoutDeteilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoutDeteilSerializer
    queryset = Noutbuk.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


