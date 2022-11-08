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
from django.urls import path
# my pages
from sections.views import home_view, contact_page, school_page, purpose_page, unique_page, motivation_page, partners_page, news_page, what_page, css, css2, jpg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('arboris/', home_view, name='homepage'),
    path('', school_page, name='schoolpage'),
    path('contact/', contact_page, name='contactpage'),
    path('our-motivation/', motivation_page, name='motivationpage'),
    path('news/', news_page, name='newspage'),
    path('partners/', partners_page, name='partnerspage'),
    path('our-purpose/', purpose_page, name='purposepage'),
    path('what-makes-us-unique/', unique_page, name='uniquepage'),
    path('what-we-do/', what_page, name='whatpage'),
    path('arboris/static/bootstrap.min.css', css, name='css'),
    path('arboris/static/fontawesome.min.css', css, name='css'),
    path('arboris/static/slick.css', css, name='css'),
    path('arboris/static/slick-theme.css', css, name='css'),
    path('arboris/static/fonts.css', css, name='css'),
    path('arboris/static/variables.css', css2, name='css'),
    path('arboris/static/styles.css', css2, name='css'),
    path('arboris/static/listings.css', css2, name='css'),
    path('arboris/static/hp.css', css2, name='css'),
    path('arboris/static/uploads/hp-banners/arboris-1.jpg', jpg, name="pic"),
    path('arboris/static/uploads/hp-banners/arboris-4.jpg', jpg, name="pic"),
    path('arboris/static/uploads/hp-banners/arboris-5.jpg', jpg, name="pic"),
]


