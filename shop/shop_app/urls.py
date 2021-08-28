from django.urls import path
from .views import *
urlpatterns = [
    path('', book_list, name='list'),
    path('<int:id>', book_detail, name='detail'),

]