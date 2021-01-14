from django.shortcuts import render
from rest_framework import viewsets
from books.models import *
from api.serializers import *

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

