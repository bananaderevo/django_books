from django.contrib import admin

from .models import Books, Order


@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
    list_display = ['book', 'author', 'description', 'image']
