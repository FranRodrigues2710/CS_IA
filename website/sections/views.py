from django.shortcuts import render
from django.http import HttpResponse
#from models import title
# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Arboris</h1>")

#def contact_page(*args, **kwargs):
 #   return HttpResponse(title.titles[6])
