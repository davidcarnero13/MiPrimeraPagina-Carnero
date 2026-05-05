from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('autor/', views.crear_autor),
    path('categoria/', views.crear_categoria),
    path('post/', views.crear_post),
    path('buscar/', views.buscar_post),
]