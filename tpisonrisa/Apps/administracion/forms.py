from django import forms
from ..tablas.models import Usuario

class registroForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nombremortal','dui','telefono','correo', 'fechanacimiento')
        widgets = {
            'nombremortal': forms.TextInput(
                attrs={'id':"nombre", 'class':"form-control",
                        'placeholder':"Nombre y Apellido", 'required':'true'}),

            'dui': forms.TextInput(
                attrs={'id':"dui", 'class':"form-control",
                       'pattern':'[0-9]{8}-[0-9]{1}', 'placeholder':"12345678-9", 'required':'true'}),
            'telefono': forms.TextInput(
                attrs={'id': "telefono", 'class': "form-control",
                       'pattern': '[0-9]{4}-[0-9]{4}', 'placeholder': "1234-5678", 'required': 'true'}),
            'correo': forms.EmailInput(
                attrs={'id': "correo", 'class': "form-control",
                       'placeholder': "Email", 'required': 'true'}),
            'fechanacimiento': forms.DateInput(
                attrs={'type':'date', 'id': 'fecha', 'class': 'form-control', 'required': 'true'}
            )
        }
        labels = {
            'nombremortal': 'Nombre', 'dui':'DUI', 'telefono':'Teléfono','fechanacimiento': 'Fecha de Nacimiento'
        }