from django.shortcuts import render
from django.http import HttpResponse
from .models import title
# Create your views here.

# context = {'data': title.objects.all()}

def home_view(request):
    context = {'request': title.objects.all()}
    return render(request, "mainpage.html", context)

def contact_page(request):
    context = {'request': title.objects.all()}
    return render(request, "contacts.html", context)
