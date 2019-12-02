from django.shortcuts import render
from django.http import HttpResponse
from tpisonrisa.Apps.tablas.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.db import connection
from django.http import JsonResponse


# Create your views here.



def incripcionTaller(request):

    try:
        id = request.session.get('id')
        nombre = request.session.get('nombre')
    except KeyError:
        pass
        return HttpResponse("You're logged out.")

    if request.method == "POST":
        id = request.session.get('id')
        usuario = Usuario.objects.get(idusuario = id)
        idtaller = request.POST.get('idtaller')
        taller = Taller.objects.get(idtaller = idtaller)
        Detalletaller(idusuario=usuario, idtaller = taller).save()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT ta.idtaller,ta.nombretaller,ta.encargado,ta.descripcion,ta.precio, ta.fecha,ta.hora,ta.max - count(dta.idusuario) as CuposDisponibles, count(dta.idusuario) as cupos, ta.max"
        " FROM taller as ta INNER JOIN detalletaller as dta USING (idtaller) group by idtaller HAVING count(dta.idusuario)< ta.max and ta.fecha > now();")
    lista = cursor.fetchall()
    cursor.close()
    context = {
        'id': id,
        'nombre': nombre,
        'lista': lista
    }
    return render(request, 'taller/inscripcionTaller.html', context)


def talleresInscrito(request):
    if 'Eliminar' in request.POST:
        id = request.session.get('id')
        usuario = Usuario.objects.get(idusuario = id)
        idtaller = request.POST.get('idtaller')
        taller = Taller.objects.get(idtaller=idtaller)
        Detalletaller.objects.filter(idusuario=usuario,idtaller=taller).delete()


    id = request.session.get('id')
    query = "SELECT ta.idtaller,ta.nombretaller,ta.encargado,ta.descripcion,ta.precio, ta.fecha,ta.hora FROM taller as ta INNER JOIN detalletaller as dta USING (idtaller) where idusuario ="+ str(id)
    query += " GROUP BY idtaller  Order BY ta.fecha desc"

    cursor = connection.cursor()
    cursor.execute(query)
    lista = cursor.fetchall()
    cursor.close()
    context = {
        'lista': lista
    }
    return render(request, 'taller/tallerInscrito.html', context)

def vol(request):
    try:
        id = request.session.get('id')
        nombre = request.session.get('nombre')
        context ={
            'id': id,
            'nombre': nombre
        }
    except KeyError:
        pass
        return HttpResponse("You're logged out.")
    return render(request, "NaviBar.html", context=context)
