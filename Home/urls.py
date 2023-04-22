##HOME

from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path("", views.home, name='Home'),
    path("Home", views.home, name='home')
]