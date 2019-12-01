from django import forms
from ..tablas.models import Peticionvisita

class visitaForm(forms.ModelForm):
    class Meta:
        model = Peticionvisita
        fields = ('nombrecontacto', 'correocontacto', 'lugardevisita', 'entidad', 'descripcion', 'fechavisita', 'horavisita')
        labels = {
            'nombrecontacto': 'Nombre', 'correocontacto': 'Correo', 'lugardevisita': 'Lugar de Visita', 'entidad':'Tipo de entidad',
            'descripcion': 'Descripción - Dirección', 'fechavisita': 'Fecha de Visita', 'horavisita': 'Hora de Visita'
        }
        widgets = {
            'nombrecontacto': forms.TextInput(
                attrs={'id': "nombre", 'class': "form-control",
                       'placeholder': "Nombre y Apellido", 'required': 'true'}),

            'lugardevisita': forms.TextInput(
                attrs={'id': "lugar", 'class': "form-control",
                       'placeholder': "Ingrese el lugar que visitará Fabrica de Sonrisas", 'required': 'true'}),
            'entidad': forms.TextInput(
                attrs={'id': "entidad", 'class': "form-control",
                       'placeholder': "Pública/Privada", 'required': 'true'}),
            'descripcion': forms.Textarea(
                attrs={'id': "telefono", 'class': "form-control",
                       'placeholder': "Ingrese una descripción y/o dirección del lugar", 'required': 'true'}),
            'correocontacto': forms.EmailInput(
                attrs={'id': "correo", 'class': "form-control",
                       'placeholder': "Ingrese un correo de contacto", 'required': 'true'}),
            'fechavisita': forms.DateInput(
                attrs={'type': 'date', 'id': 'fecha', 'class': 'form-control', 'required': 'true'}
            ),
            'horavisita': forms.TimeInput(
                attrs={'type': 'time', 'id': 'hora', 'min':'08:00', 'max':'18:00','class': 'form-control'}
            )
        }


#-------------------------LOGIN---------------------
class LoginForm(forms.Form):
   username = forms.CharField( max_length=10,widget=forms.TextInput(attrs={'type':'input', 'class':'form-control', 'id':'InputUserName', 'placeholder':'Nombre de Usuario'}))
   password = forms.CharField( max_length=35 , widget= forms.PasswordInput(attrs={'type':'password' , "class" :'form-control', 'id': 'inputPassword', 'placeholder': 'Password'}))