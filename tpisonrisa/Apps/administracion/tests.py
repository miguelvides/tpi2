from django.test import TestCase

# Create your tests here.
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tpisonrisa.settings")
django.setup()
from tpisonrisa.Apps.tablas.models import *
h1 = Usuario.objects.filter(nombresonrisero__icontains='pebbles')
if(h1):
    print("CONTIENE VALOR")
else:
    print("Vacio")
#print(str(h1[0].idhorario) +" " + h1[0].jornada)
#print(str(h1[1].idhorario) +" " + h1[1].jornada)
#print(str(h1[2].idhorario) +" " + h1[2].jornada)

print("\"Texto en Comillas\"")