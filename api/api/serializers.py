from rest_framework import serializers
from books.models import *

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')