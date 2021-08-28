from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Books, Order


class BooksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Books
        fields = ['book', 'author', 'description', 'quantity', 'image', 'id']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = Order
        fields = ['owner', 'books']
