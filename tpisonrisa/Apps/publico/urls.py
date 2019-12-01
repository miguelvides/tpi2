from django.urls import path
from . import views

urlpatterns = [
    path('peticionVisita/', views.peticionVisita, name='peticionVisita'),

    #--------------------LOGIN---------------------
    path('login/', views.loginRender, name='loginRender')


]