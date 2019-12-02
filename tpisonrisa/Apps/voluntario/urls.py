from django.urls import path
from . import views

urlpatterns = (
    path('inscripcionTaller/', views.incripcionTaller, name='inscripcionTaller'),
    path('talleresInscrito/', views.talleresInscrito, name='talleresInscrito'),
    path('solicitarRecurso/', views.peticionRecurso, name='peticionRecurso'),
)
