from django.shortcuts import render
from .forms import visitaForm, LoginForm
from ..tablas.models import Credenciales , Usuario
from ..voluntario import templates
from ..administracion import  templates

def peticionVisita(request):
    if request.method == 'POST':
        form = visitaForm(request.POST)
        if form.is_valid():
            form.save()
    form = visitaForm()
    return render(request, 'publico/peticionVisita.html', {'form': form})

def inicio(request):
    return render(request, 'publico/index.html')

#------------------[LOGIN] >><OBTENCION DE LOS DATOS Y VALIDDOR DE USUARIO -----------------------------------------------|
def loginRender(request):
    message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        usr = Credenciales.objects.filter(nombreusuario = username).filter(contrasena = request.POST.get('password'))

        if usr.exists():
            id = Credenciales.objects.get(nombreusuario = username)
            usuario = Usuario.objects.get(idusuario = id.idusuario.idusuario)
            if usuario.idtipousuario == 1:
                print(username)
                return render(request, "indexVoluntario/index.html")
            else:
                print(usuario.correo)
                return render(request, "indexAdministracion/index.html")

        else:
            message = "username o password incorrrectos"

    form = LoginForm()
    context = {
        'form' : form ,
        'message' : message,
        }

    return render( request, 'login.html', context)
