from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nonveg(response):
    return HttpResponse('<h1>Chicken Noodles</h1>')
def veg(response):
    return HttpResponse('<h1>Veg Noodles</h1>')
