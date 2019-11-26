from django.contrib import admin
from django.urls import path, include
from .Apps import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administracion/', include('tpisonrisa.Apps.administracion.urls')),
    path('publico/', include('tpisonrisa.Apps.publico.urls'))
]
