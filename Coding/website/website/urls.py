"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# my pages
from sections.views import home_view, contact_page, school_page, purpose_page, unique_page, motivation_page, create_news_page, partners_page, news_page, login_page, signup_page, read_page, what_page, css, css2, jpg, jpg2, jpg3, jpg4, jpg5, fonts, fonts2, js, js2, fonts3, fonts4, fonts5, fonts6


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/register/', signup_page, name='signup'),
    path('arboris/', home_view, name='homepage'),
    path('', school_page, name='schoolpage'),
    path('contact/', contact_page, name='contactpage'),
    path('our-motivation/', motivation_page, name='motivationpage'),
    path('news/', news_page, name='newspage'),
    path('create-news/', create_news_page, name='createnews'),
    path('partners/', partners_page, name='partnerspage'),
    path('our-purpose/', purpose_page, name='purposepage'),
    path('what-makes-us-unique/', unique_page, name='uniquepage'),
    path('what-we-do/', what_page, name='whatpage'),
    path('read/<int:my_id>', read_page, name='readpage'),
    path('arboris/static/bootstrap.min.css', css, name='css'),
    path('arboris/static/fontawesome.min.css', css, name='css'),
    path('arboris/static/slick.css', css, name='css'),
    path('arboris/static/slick-theme.css', css, name='css'),
    path('arboris/static/fonts.css', css, name='css'),
    path('arboris/static/variables.css', css2, name='css'),
    path('arboris/static/styles.css', css2, name='css'),
    path('arboris/static/listings.css', css2, name='css'),
    path('arboris/static/hp.css', css2, name='css'),
    path('arboris/static/uploads/hp-banner/arboris-1.jpg', jpg, name="pic"),
    path('arboris/static/uploads/hp-banner/arboris-4.jpg', jpg, name="pic"),
    path('arboris/static/uploads/hp-banner/arboris-5.jpg', jpg, name="pic"),
    path('arboris/static/uploads/hp-banner/logo-sm.jpg', jpg, name="pic"),
    path('arboris/static/uploads/chevron-white.svg', jpg, name="pic"),
    path('arboris/static/uploads/ajax-loader.gif', jpg2, name="pic"),
    path('arboris/static/uploads/arrow-sm-white.svg', jpg2, name="pic"),
    path('arboris/static/uploads/arrow-sm-black.svg', jpg2, name="pic"),
    path('arboris/static/uploads/lupe-white.svg', jpg2, name="pic"),
    path('arboris/static/uploads/quotation-marks.svg', jpg3, name="pic"),
    path('arboris/static/uploads/lupe.svg', jpg3, name="pic"),
    path('arboris/static/uploads/cross.svg', jpg3, name="pic"),
    path('arboris/static/uploads/hp-banner/forest-3448818.jpg', jpg3, name="pic"),
    path('arboris/static/uploads/hp-banner/forest-5442598.jpg', jpg3, name="pic"),
    path('arboris/static/uploads/hp-banner/hintersee-3601004.jpg', jpg4, name="pic"),
    path('arboris/static/uploads/hp-banner/nature-wallpaper-3622519.jpg', jpg4, name="pic"),
    path('arboris/static/uploads/hp-banner/sunset-1373171.jpg', jpg4, name="pic"),
    path('arboris/static/uploads/hp-banner/joao-rodrigues-pena.jpg', jpg4, name="pic"),
    path('arboris/static/uploads/hp-banner/joao-rodrigues-pena-arboris.jpg', jpg5, name="pic"),
    path('arboris/static/uploads/hp-banner/jose-paulo-rodrigues.jpg', jpg5, name="pic"),
    path('arboris/static/uploads/hp-banner/jose-paulo-rodrigues-arboris.jpg', jpg5, name="pic"),
    path('arboris/static/uploads/hp-banner/startup-594090.jpg', jpg5, name="pic"),
    path('arboris/static/fa_brands-400.woff2', fonts, name="font"),
    path('arboris/static/opensans-italic.woff2', fonts, name="font"),
    path('arboris/static/opensans-light.woff2', fonts, name="font"),
    path('arboris/static/opensans-regular.woff2', fonts, name="font"),
    path('arboris/static/opensanscondensed-bold.woff2', fonts, name="font"),
    path('arboris/static/opensanscondensed-light.woff2', fonts2, name="font"),
    path('arboris/static/jquery.min.js', js, name='js'),
    path('arboris/static/hp.js', js, name='js'),
    path('arboris/static/slick.min.js', js2, name='js'),
    path('arboris/static/css-vars-ponyfill.min.js', js, name='js'),
    path('arboris/static/bootstrap.bundle.min.js', js, name='js'),
    path('arboris/static/app.js', js, name='js'),
    path('arboris/static/opensans-bold.woff', fonts2, name="font"),
    path('arboris/static/OpenSans-Bold.woff2', fonts2, name="font"),
    path('arboris/static/opensans-bolditalic.woff', fonts2, name="font"),
    path('arboris/static/opensans-bolditalic.woff2', fonts2, name="font"),
    path('arboris/static/opensans-extrabold.woff', fonts3, name="font"),
    path('arboris/static/opensans-extrabold.woff2', fonts3, name="font"),
    path('arboris/static/opensans-extrabolditalic.woff', fonts3, name="font"),
    path('arboris/static/opensans-extrabolditalic.woff2', fonts3, name="font"),
    path('arboris/static/opensans-italic.woff', fonts3, name="font"),
    path('arboris/static/opensans-light.woff', fonts4, name="font"),
    path('arboris/static/opensans-lightitalic.woff', fonts4, name="font"),
    path('arboris/static/opensans-lightitalic.woff2', fonts4, name="font"),
    path('arboris/static/opensans-regular.woff', fonts4, name="font"),
    path('arboris/static/opensans-semibold.woff', fonts4, name="font"),
    path('arboris/static/opensans-semibold.woff2', fonts5, name="font"),
    path('arboris/static/opensans-semibolditalic.woff', fonts5, name="font"),
    path('arboris/static/opensans-semibolditalic.woff2', fonts5, name="font"),
    path('arboris/static/opensanscondensed-bold.woff', fonts5, name="font"),
    path('arboris/static/opensanscondensed-light.woff', fonts5, name="font"),
    path('arboris/static/opensanscondensed-lightitalic.woff', fonts6, name="font"),
    path('arboris/static/opensanscondensed-lightitalic.woff2', fonts6, name="font"),

]