from django import forms
from django.forms import ModelForm
from .models import Colaborador


class colaboraForm(ModelForm):

    class Meta:
        model = Colaborador
        fields = ['rut', 'fotop', 'nombre', 'celular',
                  'direccion', 'correo', 'pais', 'contraseña']

        labels = {
            'rut': 'RUT ',
            'fotop': 'Foto Perfil ',
            'nombre': 'Nombre Completo ',
            'celular': 'Teléfono ',
            'direccion': 'Dirección ',
            'correo': 'Correo Electrónico ',
            'pais': 'País ',
            'contraseña': 'Contraseña '

        }
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut',
                    'name': 'rut',
                    'placeholder': '12345678-9'
                }
            ),
            'fotop': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fotop',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                    'name': 'nombre'
                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'celular',
                    'name': 'celular',
                    'placeholder': '+56912345678'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'name': 'direccion'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'correo',
                    'name': 'email',
                    'placeholder': 'Ejemplo@ejemplo.cl'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'pais',
                    'name': 'pais',
                    'placeholder': 'Ej: Chile'
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'password',
                    'name': 'password'
                }
            ),
        }
