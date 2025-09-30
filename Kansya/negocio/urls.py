from django.urls import path
from . import views

urlpatterns = [
    path('iniciar-negocio/', views.CrearNegocio, name='iniciar_negocio'),
]
