from django.contrib import admin
from django.urls import path, include
from .Apps import *
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('administracion/', include('tpisonrisa.Apps.administracion.urls')),
    path('publico/', include('tpisonrisa.Apps.publico.urls')),
    path('voluntario/', include('tpisonrisa.Apps.voluntario.urls')),
    path('publico/', include('tpisonrisa.Apps.publico.urls')),
    path('', views.index, name='inicio'),

]
