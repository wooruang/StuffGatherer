from django.shortcuts import render
from rest_framework import generics

from .models import Data
from .serializers import DataSerializer


class ListPost(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
