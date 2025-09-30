from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('registro-admin/', views.RegistrarAdmin, name='registro_admin'),
    path('registro-empleado/', views.RegistrarEmpleado, name='registro_empleado'),
]
