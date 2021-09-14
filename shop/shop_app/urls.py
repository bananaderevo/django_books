from django.urls import path
from .views import *
urlpatterns = [
    path('', book_list, name='list'),
    path('<int:id>', book_detail, name='detail'),
    path('profile/', profile, name='profile'),
    path('profile/edit', update_profile, name='profile_edit'),
    path('cart/', cart, name='cart'),

]