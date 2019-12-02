from django.http import HttpResponse
from .serializers import *
from django.shortcuts import render
from django.db import connection

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

def peticionRecurso(request):
    id2 = request.session.get('id')
    if 'agregar' in request.POST:
        id = request.POST.get('id')
        Solicitudrecurso(idusuario=Usuario.objects.get(idusuario=id2), recursosonrisero=Recursosonriseros.objects.get(idrecurso=id)).save()
        print("agregado")

    if 'eliminar' in request.POST:
        idEliminar = request.POST.get('eid')
        Solicitudrecurso.objects.filter(idsolicitudrecurso=idEliminar).delete()


    cursor = connection.cursor()
    cursor.execute("SELECT so.idsolicitudrecurso, us.nombresonrisero, re.nombrerecurso, re.talla, so.pago "
                   "FROM solicitudrecurso AS so "
                   "INNER JOIN recursosonriseros AS re ON so.recursosonrisero = re.idrecurso "
                   "INNER JOIN usuario AS us USING(idusuario) WHERE us.idusuario = "+str(id2))
    lista = cursor.fetchall()
    cursor.close()

    cursor2 = connection.cursor()
    cursor2.execute("SELECT * FROM recursosonriseros")
    lista2 = cursor2.fetchall()
    cursor2.close()

    context = {
        'lista': lista,
        'lista2': lista2,
    }
    return render(request, 'recurso/peticionRecurso.html', context)
