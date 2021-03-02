from django.shortcuts import render
from rest_framework import viewsets
from .models import Items
from .serializers import ItemsSerializer

# Create your views here.
class ItemsView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer