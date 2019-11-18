from django.urls import path
from . import views

urlpatterns = [

    # path('administrador/', admin.site.urls),
    path('', views.index, name='index'),
    path('aspirante/', views.aspirante, name='aspirante'),
    path('aspirante/<int:id>/', views.detail, name='detail'),
    path('bs/', views.boostrap, name='detail'),

    path('eventos/', views.listadoEvento, name='eventos'),
    path('eventos/voluntarios', views.eventosVoluntarios, name='eventosVoluntarios'),
    path('eventosDisponibles/', views.eventosDisponibles, name='eventosDisponibles'),
    path('talleresDisponibles/', views.talleresDisponibles, name='talleresDisponibles'),
    path('detalleTaller/', views.detalleTaller, name='detalleTaller'),

    # LISTADO JSON
    # Aspirantes sin nombre sonrisero
    path('aspirante/listado/', views.listadoAspirante, name='lst_aspirante'),
    path('aspirante/update/', views.update_aspirante, name='update_aspirante'),
    path('aspirante/delete/', views.delete_aspirante, name='aspirante'),
    path('aspirante/create/', views.post_aspirante, name='aspirante'),

]
