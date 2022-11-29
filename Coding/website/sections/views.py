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

def purpose_page(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=1)
               }
    return render(request, "contacts.html", context)

def unique_page(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=3)
               }
    return render(request, "contacts.html", context)

def motivation_page(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=2)
               }
    return render(request, "contacts.html", context)

def partners_page(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=5)
               }
    return render(request, "contacts.html", context)

def news_page(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=7)
               }
    return render(request, "contacts.html", context)

def what_page(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=4)
               }
    return render(request, "contacts.html", context)

def css(request):
    return render(request, "bootstrap.min.css", "fontawesome.min.css", "slick.css", "slick-theme.css", "fonts.css")

def css2(request):
    return render(request, "variables.css", "styles.css", "listings.css", "static/hp.css")

def jpg(request):
    return render(request, "arboris-1.jpg", "arboris-4.jpg", "arboris-5.jpg", "logo-sm.jpg", "chevron-white.svg", )

def test(request):
    context = {'results': title.objects.all(),
               'header': title.objects.get(id=8)
               }
    return render(request, 'test.html', context)