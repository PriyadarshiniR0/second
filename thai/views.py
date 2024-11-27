from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def tnonveg(response):
    return HttpResponse('<h1>Chicken Soup</h1>')
def tveg(response):
    return HttpResponse('<h1>Veg Soup</h1>')