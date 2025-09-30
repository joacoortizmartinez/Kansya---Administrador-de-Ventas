from django.contrib import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path('abrir-caja/', views.AbrirCaja, name='abrir_caja'),
]
