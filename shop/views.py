from django.shortcuts import render
from django.http import HttpResponse

from . models import Item, Purchase


def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')

