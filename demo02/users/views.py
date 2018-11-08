from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def hello(request, a, b):
    url = reverse('usersspace:hello')
    print(url)
    print(a, b)
    return HttpResponse('hello django')


def demo_view(request):
    print('demo_view are called')
    return HttpResponse('ok')
