##HOME

from django.contrib import admin
from django.urls import path
from Home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.home, name='Home'),
    path("Home", views.home, name='home')
]

urlpatterns += staticfiles_urlpatterns()
