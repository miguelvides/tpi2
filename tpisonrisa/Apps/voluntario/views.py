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

    cursor = connection.cursor()
    cursor.execute(
        "SELECT ta.idtaller,ta.nombretaller,ta.encargado,ta.descripcion,ta.precio, ta.fecha,ta.hora,ta.max - count(dta.idusuario) as CuposDisponibles, count(dta.idusuario) as cupos, ta.max"
        " FROM taller as ta INNER JOIN detalletaller as dta USING (idtaller) group by idtaller HAVING count(dta.idusuario)< ta.max and ta.fecha > now();")
    lista = cursor.fetchall()
    cursor.close()
    context = {
        'lista': lista
    }
    return render(request, 'taller/inscripcionTaller.html', context)


def talleresInscrito(request):
    query = "SELECT ta.idtaller,ta.nombretaller,ta.encargado,ta.descripcion,ta.precio, ta.fecha,ta.hora FROM taller as ta INNER JOIN detalletaller as dta USING (idtaller) where idusuario = 2"
    query += "GROUP BY idtaller  Order BY ta.fecha desc"

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
