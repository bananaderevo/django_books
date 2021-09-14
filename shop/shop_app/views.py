from django.shortcuts import render, get_object_or_404, redirect
import requests
import json
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cart
from .forms import UpdateProfile
from django.contrib.auth.decorators import login_required


def book_list(request):
    data1 = requests.get(r'http://127.0.0.1:8000/')
    data = json.loads(data1.text)
    p = data['results']
    return render(request, 'shop/main.html', {'data': p})


def book_detail(request, id):

    data1 = requests.get(f'http://127.0.0.1:8000/{id}')
    data = json.loads(data1.text)
    p = data
    l = [p]
    if request.method == 'POST':
        try:
            books = Cart.objects.get(customer=request.user).books
            if p['book'] not in books:
                Cart.objects.update(customer=request.user,
                                    books=list(books).append(p))
        except Cart.DoesNotExist:
            Cart.objects.get_or_create(customer=request.user,
                                       books=l)

    return render(request, 'shop/detail.html', {'data': p})


class HttpResponseRedirect:
    pass


@login_required(login_url="/login")
def update_profile(request):
    instance = request.user
    form = UpdateProfile(request.POST or None, instance=instance)
    user = request.user
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'user/user_profile_edit.html', {'form': form,
                                                           'user': user})


@login_required(login_url="/login")
def profile(request):
    user = request.user
    return render(request, 'user/user_profile.html', {'user': user})


@login_required(login_url="/login")
def cart(request):
    cart = Cart.objects.get(customer=request.user)
    return render(request, 'shop/cart.html', {'cart': cart})
