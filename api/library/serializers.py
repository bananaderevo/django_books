from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Books, Order


class BooksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Books
        fields = ['book', 'author', 'price', 'genre', 'description', 'quantity', 'image', 'id']


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ['owner', 'books', 'total']
