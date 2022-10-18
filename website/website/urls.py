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
from sections.views import home_view, contact_page, school_page, purpose_page, unique_page, motivation_page, partners_page, news_page, what_page



urlpatterns = [
    path('admin/', admin.site.urls),
    path('arboris/', home_view, name='homepage'),
    path('', school_page, name='schoolpage'),
    path('contact/', contact_page, name='contactpage'),
    path('motivation/', motivation_page, name='motivationpage'),
    path('news/', news_page, name='newspage'),
    path('partners/', partners_page, name='partnerspage'),
    path('purpose/', purpose_page, name='purposepage'),
    path('unique/', unique_page, name='uniquepage'),
    path('what/', what_page, name='whatpage'),
]
