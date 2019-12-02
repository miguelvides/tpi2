from django.urls import path
from . import views

urlpatterns = (

    path('inscripcionTaller/', views.incripcionTaller, name='inscripcionTaller'),
    path('talleresInscrito/', views.talleresInscrito, name='talleresInscrito'),
    path('detalle-visita/',views.detalleVisita, name='detalleTaller'),
    path('peticion-visita/',views.peticionvisita, name='peticion'),
    path('solicitudRecurso/',views.solicitudrecurso, name='Recurso'),
  



)
