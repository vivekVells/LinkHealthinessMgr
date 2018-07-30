from django.shortcuts import render
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verifyByFile', views.verifyByFile, name='verifyByFile'),
    path('verifyByUrl', views.verifyByUrl, name='verifyByUrl'),
]
