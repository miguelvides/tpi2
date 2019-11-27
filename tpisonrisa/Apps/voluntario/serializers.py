from rest_framework import serializers
from tpisonrisa.Apps.tablas.models import *


class ListaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['idusuario']
        # fields = '__all__'
        # fields = ('__all__')
        # fields =  ['nombresonrisero']


class campos_Usuario(serializers.Serializer):
    sonrisero = serializers.CharField()
    generacion = serializers.CharField()
    tipo = serializers.CharField()
    constelacion = serializers.CharField()
    id = serializers.IntegerField()


