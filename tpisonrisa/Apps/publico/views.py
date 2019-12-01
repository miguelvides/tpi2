from django.shortcuts import render
from .forms import visitaForm, LoginForm
from ..tablas.models import *
from django.db import connection
from tpisonrisa.Apps.voluntario.views import *


def peticionVisita(request):
    if request.method == 'POST':
        form = visitaForm(request.POST)
        if form.is_valid():
            form.save()
    form = visitaForm()
    return render(request, 'publico/peticionVisita.html', {'form': form})


def inicio(request):
    return render(request, 'publico/index.html')


# ------------------[LOGIN] >><OBTENCION DE LOS DATOS Y VALIDDOR DE USUARIO -----------------------------------------------|
def loginRender(request):
    message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('password')
        usr = Credenciales.objects.filter(nombreusuario=username, contrasena=passw)
        print("METODO POST")
        print(str(username))
        print(str(passw))

        if usr.exists():
            print("Existe")
            cursor = connection.cursor()
            cursor.execute("SELECT idtipousuario, nombresonrisero, idusuario FROM usuario WHERE nombresonrisero ILIKE '"+username+"'")
            idtipo = cursor.fetchall()
            print(idtipo)
            print(idtipo[0][0])
            print(idtipo[0][1])


            if (idtipo[0][0]==1):
                #Voluntario
                context = {
                    'acceso': idtipo
                }
                request.session['id'] = idtipo[0][2]
                request.session['nombre'] = idtipo[0][1]
                return vol(request)
            elif (idtipo[0][0]>=2 and idtipo[0][0]<=4):
                # Administradores
                request.session['id'] = idtipo[0][2]
                request.session['nombre'] = idtipo[0][1]
                context = {
                    'acceso': idtipo
                }
            else:
                print("como llegaste aqui")
        else:

            print("NO Existe")
            message = "username o password incorrrectos"

            message = "Nombre de Usuario o Contraseña incorrrectos"

    form = LoginForm()
    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'login.html', context)
