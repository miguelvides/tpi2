from django.urls import path
from . import views

urlpatterns = [
    path('peticionVisita/', views.peticionVisita, name='peticionVisita'),
    path('', views.inicio, name='inicio'),

    #--------------------LOGIN---------------------
    path('login/', views.loginRender, name='loginRender')


]