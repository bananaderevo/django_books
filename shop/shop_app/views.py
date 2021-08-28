from django.shortcuts import render
import requests
import json


def book_list(request):
    data1 = requests.get(r'http://127.0.0.1:8000/')
    data = json.loads(data1.text)
    p = data['results']
    return render(request, 'shop/main.html', {'data': p})


def book_detail(request, id):
    data1 = requests.get(f'http://127.0.0.1:8000/{id}')
    data = json.loads(data1.text)
    p = data
    return render(request, 'shop/detail.html', {'data': p})