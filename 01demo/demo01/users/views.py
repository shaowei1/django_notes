from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    """
    index view
    :param request: include request information of request object
    :return: response object
    """
    print("*" * 50)
    print(request)
    print("*" * 50)

    return HttpResponse("hello Django!")


def say(request):
    url = reverse('usersnamespace:sayname')
    print(url)
    return HttpResponse('say')


def sayhello(request):
    return HttpResponse('sayhello')
