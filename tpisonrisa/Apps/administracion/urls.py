from django.urls import path
from . import views

urlpatterns = [
    # path('administrador/', admin.site.urls),
    path('', views.index, name='index'),
    path('aspirante/', views.aspirante, name='aspiranteV'),
    path('evento/', views.listadoEvento, name='eventos'),
    path('detalleEvento/', views.eventosVoluntarios, name='eventosVoluntarios'),
    path('detalleTaller/', views.detalleTaller, name='detalleTaller'),
    path('recursos/', views.crudRecurso, name='recursos'),
    path('registroAspirante/', views.registroAspirante, name='registroAspirante'),
    path('detalleRecursos/', views.detalleRecurso, name='detalleRecursos'),

    path('aspirante/<int:id>/', views.detail, name='detail'),
    path('bs/', views.boostrap, name='detail'),

    path('eventosDisponibles/', views.eventosDisponibles, name='eventosDisponibles'),
    path('talleresDisponibles/', views.talleresDisponibles, name='talleresDisponibles'),
    path('crearTaller/', views.crearTaller, name='crearTaller'),
    path('logout/', views.logout, name='logout'),

    # LISTADO JSON
    # Aspirantes sin nombre sonrisero
    path('aspirante/listado/', views.listadoAspirante, name='lst_aspirante'),
    path('aspirante/update/', views.update_aspirante, name='update_aspirante'),
    path('aspirante/delete/', views.delete_aspirante, name='aspirante2'),
    path('aspirante/create/', views.post_aspirante, name='create_aspirante'),

]
