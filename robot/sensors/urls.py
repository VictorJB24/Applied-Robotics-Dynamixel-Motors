from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('reflectance', views.reflectance, name='reflectance'),
    path('distance', views.distance, name='distance'),
]