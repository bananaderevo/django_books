from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class AdminBooks(admin.ModelAdmin):
    list_display = ['customer', 'books']
