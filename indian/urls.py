from indian.views import*
from django.urls import path

urlpatterns = [
    path('nonveg/',nonveg,name='nonveg'),
    path('veg/',veg,name='veg')

]
