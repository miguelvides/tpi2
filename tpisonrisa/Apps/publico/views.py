from django.shortcuts import render
from .forms import visitaForm

def peticionVisita(request):
    if request.method == 'POST':
        form = visitaForm(request.POST)
        if form.is_valid():
            form.save()
    form = visitaForm()
    return render(request, 'publico/peticionVisita.html', {'form': form})

def inicio(request):
    return render(request, 'publico/index.html')
