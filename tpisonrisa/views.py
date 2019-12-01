from tpisonrisa.Apps.tablas.models import *
from django.shortcuts import render


def index(request):
    if 'Eliminar' in request.POST:
        id = request.POST.get('idEliminar')
        Usuario.objects.filter(idusuario=id).delete()

    filtro = Usuario.objects.filter(nombresonrisero__isnull=True)
    constelacion = Constelacion.objects.all().order_by('idconstelacion')
    tipo = Tipousuario.objects.all().order_by('idtipousuario')

    context = {
        'aspirante_list': filtro,
        'tipo': tipo,
        'constelacion': constelacion
    }
    return render(request, 'indice.html', context)