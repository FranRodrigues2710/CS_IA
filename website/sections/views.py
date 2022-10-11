from django.shortcuts import render
from django.http import HttpResponse
from .models import title
# Create your views here.

def home_view(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=8)
               }
    return render(request, "mainpage.html", context)

def contact_page(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=6)
               }
    return render(request, "contacts.html", context)

def school_page(request):
    return render(request, "schoolpage.html", {})
