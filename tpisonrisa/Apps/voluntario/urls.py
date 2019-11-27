from django.urls import path
from . import views

urlpatterns = (

    path('inscripcion-taller/', views.incripcionTaller, name='inscripcionTaller'),
    path('talleres-inscrito/', views.talleresInscrito, name='talleresInscrito'),
)
