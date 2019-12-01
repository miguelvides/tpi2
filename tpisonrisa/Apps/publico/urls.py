from django.urls import path
from . import views

urlpatterns = [
    path('peticionVisita/', views.peticionVisita, name='peticionVisita'),
<<<<<<< HEAD
=======
    path('', views.inicio, name='inicio'),

>>>>>>> 717e590650a573f343254613d8dd9dfa26c973d1
    #--------------------LOGIN---------------------
    path('login/', views.loginRender, name='loginRender')


]