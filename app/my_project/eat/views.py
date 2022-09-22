from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def to_eat(request):
    return HttpResponse('<h1>Что покушать</h1>')
