from django.db import models


class Books(models.Model):
    book = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Order(models.Model):
    owner = models.CharField(max_length=100)
    books = models.TextField()
