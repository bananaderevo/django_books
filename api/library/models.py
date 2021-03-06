from django.db import models


class Books(models.Model):
    book = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images')
    price = models.FloatField()
    genre = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']
        verbose_name = 'Book'

    def __str__(self):
        return self.book


class Order(models.Model):
    owner = models.CharField(max_length=100)
    books = models.TextField()
    total = models.FloatField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Orders'

    def __str__(self):
        return self.books
