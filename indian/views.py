from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nonveg(request):
    return HttpResponse("<h1>Biryani,<marquee>Chicken 65,gravy,tandoori</marquee></h1>")
def veg(request):
    return HttpResponse("<h1> Idli,Dosa,Vada,Sambhar</h1>")
