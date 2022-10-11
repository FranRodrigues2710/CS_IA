from django.shortcuts import render
from django.http import HttpResponse
from .models import title
# Create your views here.

def home_view(request):
    context = {'results': title.objects.all()}
    return render(request, "mainpage.html", context)

def contact_page(request):
    context = {'results': title.objects.all()}
    return render(request, "contacts.html", context)
