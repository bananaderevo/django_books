from django.shortcuts import render, get_object_or_404, redirect
import requests
import json
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cart
from .forms import UpdateProfile
from django.contrib.auth.decorators import login_required
import ast


def book_list(request):
    data1 = requests.get(r'http://127.0.0.1:8000/list/')
    data = json.loads(data1.text)
    p = data['results']
    return render(request, 'shop/main.html', {'data': p})


def book_detail(request, id):

    data1 = requests.get(f'http://127.0.0.1:8000/list/{id}')
    data = json.loads(data1.text)
    p = data
    print(p)
    if request.method == 'POST':
        try:
            books = Cart.objects.get(customer=request.user).books
            if p['book'] not in books:
                c = Cart.objects.get(customer=request.user)
                if books:
                    c.books = f"{books} ; {p}"
                else:
                    c.books = str(p)
                c.save()

        except Cart.DoesNotExist:
            Cart.objects.get_or_create(customer=request.user,
                                       books=str(p))

    return render(request, 'shop/detail.html', {'data': p,
                                                'user': request.user})


def item_delete(request, id):
    cart = Cart.objects.get(customer=request.user).books.split(' ; ')
    print(cart)
    print('\n---------------------------\n')

    for i in cart:
        i = ast.literal_eval(i)
        if i['id'] == id:
            cart.remove(str(i))

    print(cart)

    final = Cart.objects.get(customer=request.user)
    final.books = ' ; '.join(cart)
    final.save()

    return redirect('/cart/')


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
    total = 0
    cart = Cart.objects.get(customer=request.user)
    d = Cart.objects.get(customer=request.user).books.split(' ; ')
    p = []
    for i in d:
        i = ast.literal_eval(i)
        total += float(i['price'])
        p.append(i)

    if request.method == 'POST':
        # curl - X
        # POST - S - H - u
        # "admin:password" - F
        # "file=@img.jpg;type=image/jpg"
        # 127.0
        # .0
        # .1: 8000 / resourceurl / imageUpload
        requests.post(r'http://127.0.0.1:8000/order/', data={'a:a'}, json={
            "owner": request.user.username,
            "books": p,
            "total": total
        })

    return render(request, 'shop/cart.html', {'cart': cart,
                                              'books': p,
                                              'total': total})
