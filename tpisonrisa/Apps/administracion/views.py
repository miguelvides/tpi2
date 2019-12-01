from django.http import HttpResponse
from tpisonrisa.Apps.tablas.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse


@api_view(['GET', ])
def listadoAspirante(request):
    try:
        lista = Usuario.objects.filter(nombresonrisero__isnull=True)
        # lista = Usuario.objects.all()
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ListaUsuarioSerializer(lista, many=True)
        return Response(serializer.data)


@api_view(['PUT', ])
def update_aspirante(request):
    try:
        lista = Usuario.objects.filter(nombresonrisero__isnull=True)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = ListaUsuarioSerializer(lista, data=request.data)
        data = {
        }
        if serializer.is_valid():
            serializer.save()
            data["succes"] = "Nuevo Miembro Ingresado"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def delete_aspirante(request):
    try:
        lista = Usuario.objects.filter(nombresonrisero__isnull=True)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = lista.delete()
        data = {
        }
        if operation:
            data["succes"] = "Aspirante Eliminado"
        else:
            data["failure"] = "Error Eliminar"
        return Response(data=data)


@api_view(['POST', ])
def post_aspirante(request):
    # cuenta = Usuario.objects.get(idusuario=2)
    if request.method == "POST":
        # serializer = ListaUsuarioSerializer(cuenta, data=request.data)
        serializer = campos_Usuario(data=request.data)
        if serializer.is_valid():
            u = Usuario.objects.filter(nombresonrisero__icontains=serializer.data.get('sonrisero'))
            t = Tipousuario.objects.get(descripcion=serializer.data.get('tipo'))
            c = Constelacion.objects.get(descripcionconstelacion=serializer.data.get('constelacion'))
            if (u):
                return Response({'message': 'Nombre Sonrisero no disponible'}, status=status.HTTP_302_FOUND)
            else:
                Usuario.objects.filter(idusuario=serializer.data.get('id')).update(
                    nombresonrisero=serializer.data.get('sonrisero'), idtipousuario=t, idconstelacion=c)
                return Response({'message': 'Elemento Actualizado'}, status=status.HTTP_201_CREATED)
            print(serializer)
        return Response({'message': 'Oops ocurrio un error'}, status=status.HTTP_400_BAD_REQUEST)


def eventosVoluntarios(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT p.lugardevisita, p.horavisita, p.fechavisita, p.descripcion ,u.nombresonrisero, es.descripcionestado, es.idestado "
        "FROM detallevisita as d INNER JOIN usuario as u "
        "USING(idusuario) INNER JOIN peticionvisita as p "
        "USING(idpeticionvisita) INNER JOIN estado as es USING (idestado) ORDER BY p.lugardevisita ASC")
    lista = cursor.fetchall()
    cursor.close()
    context = {
        'lista': lista
    }
    return render(request, 'visita/eventoVoluntarios.html', context)


def detalleTaller(request):
    if request.method == 'POST':
        id = request.POST.get('idestado')
        Detalletaller.objects.filter(iddetalletaller=id).update(pago=1)

    cursor = connection.cursor()
    cursor.execute("SELECT d.iddetalletaller, ta.nombretaller, ta.descripcion, ta.fecha, u.nombresonrisero, d.pago "
                   "FROM detalletaller AS d INNER JOIN taller AS ta USING (idtaller) "
                   "INNER JOIN usuario AS u USING (idusuario)")
    lista = cursor.fetchall()
    cursor.close()
    context = {
        'lista': lista
    }
    return render(request, 'taller/detalleTaller.html', context)


def listadoEvento(request):
    if request.method == 'POST':
        id = request.POST.get('idvisita')
        estado = request.POST.get('e')
        idestado = Estado.objects.filter(descripcionestado=str(estado))[0].idestado
        Peticionvisita.objects.filter(idpeticionvisita=id).update(idestado=idestado)

    cursor = connection.cursor()
    cursor.execute("SELECT pe.idpeticionvisita, pe.entidad, pe.nombrecontacto, pe.correocontacto, "
                   "pe.fechavisita, pe.horavisita, pe.lugardevisita, e.descripcionestado, e.idestado, pe.descripcion "
                   "FROM peticionvisita AS pe INNER JOIN estado AS e USING (idestado)")
    lista = cursor.fetchall()
    estado = Estado.objects.all()
    context = {
        'lista': lista,
        'estado': estado
    }
    return render(request, 'visita/evento.html', context)


def talleresDisponibles(request):
    cursor = connection.cursor()
    cursor.execute("SELECT d.iddetalletaller, ta.nombretaller, ta.descripcion, ta.fecha, u.nombresonrisero, d.pago "
                   "FROM detalletaller AS d INNER JOIN taller AS ta USING (idtaller) "
                   "INNER JOIN usuario AS u USING (idusuario)")
    lista = cursor.fetchall()
    cursor.close()
    return JsonResponse(lista, safe=False)


def eventosDisponibles(request):
    cursor = connection.cursor()
    cursor.execute("SELECT p.entidad, p.nombrecontacto, p.correocontacto, "
                   "p.fechavisita, p.horavisita, p.lugardevisita, e.descripcionestado "
                   "FROM peticionvisita AS p INNER JOIN estado AS e USING(idestado) ORDER BY p.idestado ASC")
    lista = cursor.fetchall()
    cursor.close()
    return JsonResponse(lista, safe=False)


def index(request):
    all_usuarios = Usuario.objects.all()
    html = ''
    for u in all_usuarios:
        url = '/administracion/aspirante/' + str(u.idusuario) + '/'
        html += '<a href ="' + url + '">' + u.nombremortal + '</a><br>'
    return HttpResponse(html)


def aspirante(request):
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
    return render(request, 'aspirante/aspirante.html', context)


def detail(request, id):
    p = get_object_or_404(Usuario, idusuario=id, nombresonrisero__isnull=True)
    if request.method == 'POST':
        name_sonrisero = request.POST.get('sonrisero')
        rs = Usuario.objects.filter(nombresonrisero__icontains=name_sonrisero)
        if rs:
            messages.warning(request, 'Nombre Sonrisero ' + name_sonrisero + ' no disponible.')
            # print("EL NOMBRE SONRISERO "+str(d))

    constelacion = Constelacion.objects.all().order_by('idconstelacion')
    tipo = Tipousuario.objects.all().order_by('idtipousuario')

    return render(request, 'aspirante/edtAspirante.html', {'dato': p, 'c': constelacion, 't': tipo})


def boostrap(request):
    if request.method == 'POST':
        d = request.POST.get('c1')
        print('Ey Carlos estoy aqui ' + d)

    filtro = Usuario.objects.filter(nombresonrisero__isnull=True)
    context = {
        'aspirante_list': filtro,
    }
    return render(request, 'aspirante/pBoostrap.html', context)


def crudRecurso(request):
    if 'Agregar' in request.POST:
        recurso = request.POST.get('recurso')
        detalle = request.POST.get('detalle')
        precio = request.POST.get('precio')
        print(precio)
        Recursosonriseros(nombrerecurso=recurso, talla=detalle, preciorecurso=precio).save()

    if 'Editar' in request.POST:
        print('ENTRO A EDITAR')
        id = request.POST.get('id')
        recurso = request.POST.get('recurso')
        detalle = request.POST.get('detalle')
        precio = request.POST.get('precio')
        Recursosonriseros.objects.filter(idrecurso=id).update(nombrerecurso=recurso, talla=detalle, preciorecurso=precio)

    if 'Eliminar' in request.POST:
        print('ENTRO A ELIMINAR')
        id = request.POST.get('id')
        Recursosonriseros.objects.filter(idrecurso=id).delete()

    recursos = Recursosonriseros.objects.all()
    context = {
        'recursos': recursos,
    }
    return render(request, 'recursos/recursos.html', context)

def detalleRecurso(request):
    if request.method == 'POST':
        id = request.POST.get('idestado')
        Solicitudrecurso.objects.filter(idsolicitudrecurso=id).update(pago=1)

    cursor = connection.cursor()
    cursor.execute("SELECT so.idsolicitudrecurso, us.nombresonrisero, re.nombrerecurso, re.talla, so.pago "
                   "FROM solicitudrecurso AS so "
                   "INNER JOIN recursosonriseros AS re ON so.recursosonrisero = re.idrecurso "
                   "INNER JOIN usuario AS us USING(idusuario)")
    lista = cursor.fetchall()
    cursor.close()
    context = {
        'lista': lista
    }
    return render(request, 'recursos/detalleRecurso.html', context)
