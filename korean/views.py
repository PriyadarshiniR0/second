from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nonveg(request):
    return HttpResponse("<h1><marquee>Korean fried chicken,Gimbap </marquee></h1>")
def veg(request):
    return HttpResponse("<h1> Ramen,Kimchi,Bibimbap</h1>")

