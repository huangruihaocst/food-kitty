"""FoodKitty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from FoodKittyApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^FoodKitty/search$', views.search, name='search'),
    url(r'^FoodKitty/results/$', views.results, name="results"),
    url(r'^FoodKitty/details/(.*?)$', views.details, name='details'),
    url(r'^FoodKitty/advanced$', views.advanced, name='advanced'),
    url(r'^FoodKitty/advanced_results/$', views.advanced_search, name="advanced_results"),
    url(r'^FoodKitty/about$', views.about, name="about"),
    url(r'^FoodKitty/help$', views.for_help, name="help")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
