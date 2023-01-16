from django.shortcuts import render
from django.http import HttpResponse
from .models import news
# Create your views here.

def home_view(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=8)
               }
    return render(request, "mainpage.html", context)

def contact_page(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=6)
               }
    return render(request, "contacts.html", context)

def school_page(request):
    return render(request, "schoolpage.html", {})

def purpose_page(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=1)
               }
    return render(request, "purpose.html", context)

def unique_page(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=3)
               }
    return render(request, "unique.html", context)

def motivation_page(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=2)
               }
    return render(request, "motivation.html", context)

def partners_page(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=5)
               }
    return render(request, "partners.html", context)

def news_page(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=7),
               'title1': news.objects.get(),
               'paragraph1': news.objects.get(),
               'paragraph2': news.objects.get(),
               'image': news.objects.get(),
               }
    return render(request, "news.html", context)

def login_page(request):
    context = {'results': news.objects.all(),

               }
    return render(request, "news.html", context)
def what_page(request):
    context = {'results': news.objects.all(),
               'header': news.objects.get(id=4)
               }
    return render(request, "whatdo.html", context)

def css(request):
    return render(request, "bootstrap.min.css", "fontawesome.min.css", "slick.css", "slick-theme.css", "fonts.css")

def css2(request):
    return render(request, "variables.css", "styles.css", "listings.css", "static/hp.css")

def jpg(request):
    return render(request, "arboris-1.jpg", "arboris-4.jpg", "arboris-5.jpg", "logo-sm.jpg", "chevron-white.svg")

def jpg2(request):
    return render(request, "ajax-loader.gif", "arrow-sm-white.svg", "lupe-white.svg", "arrow-sm-black.svg", "arrow-link-gold.svg")

def jpg3(request):
    return render(request, "cross.svg", "lupe.svg", "quotation-marks.svg", "forest-3448818.jpg", "forest-5442598.jpg")

def jpg4(request):
    return render(request, "hintersee-3601004.jpg", "nature-wallpaper-3622519.jpg", "sunset-1373171.jpg", "joao-rodrigues-pena.jpg")

def jpg5(request):
    return render(request, "joao-rodrigues-pena-arboris.jpg", "jose-paulo-rodrigues.jpg", "jose-paulo-rodrigues-arboris.jpg", "startup-594090.jpg")

def fonts(request):
    return render(request, "fa-brands-400.woff2", "opensans-italic.woff2", "opensans-light.woff2", "opensans-regular.woff2", "opensanscondensed-bold.woff2")

def fonts2(request):
    return render(request, "opensanscondensed-light.woff2", "opensans-bold.woff", "OpenSans-Bold.woff2", "opensans-bolditalic.woff", "opensans-bolditalic.woff2")

def fonts3(request):
    return render(request, "opensans-extrabold.woff", "opensans-extrabold.woff2", "opensans-extrabolditalic.woff", "opensans-extrabolditalic.woff2", "opensans-italic.woff")

def fonts4(request):
    return render(request, "opensans-light.woff", "opensans-lightitalic.woff", "opensans-lightitalic.woff2", "opensans-regular.woff", "opensans-semibold.woff")

def fonts5(request):
    return render(request, "opensans-semibold.woff2", "opensans-semibolditalic.woff", "opensans-semibolditalic.woff2", "opensanscondensed-bold.woff", "opensanscondensed-light.woff")

def fonts6(request):
    return render(request, "opensanscondensed-lightitalic.woff", "opensanscondensed-lightitalic.woff2")
def js(request):
    return render(request, "app.js", "bootstrap.bundle.min.js", "css-vars-ponyfill.min.js", "hp.js", "jquery.min.js")

def js2(request):
    return render(request, "slick.min.js")
