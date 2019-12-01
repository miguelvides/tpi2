from django.urls import path
from . import views

urlpatterns = [
    path('peticionVisita/', views.peticionVisita, name='peticionVisita'),
<<<<<<< HEAD

=======
>>>>>>> cdc087509df3c600651993b66d7fa2c3d0378789
    path('', views.inicio, name='inicio'),


    #--------------------LOGIN---------------------
    path('login/', views.loginRender, name='loginRender')


]