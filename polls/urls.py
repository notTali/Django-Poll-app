from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('polls', views.home),
    path('about', views.about),
]