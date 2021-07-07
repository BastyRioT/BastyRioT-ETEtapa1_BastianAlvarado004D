from django.db import models

# Create your models here.


class Colaborador(models.Model):

    rut = models.CharField(
        primary_key=True, max_length=10, verbose_name='Rut colaborador')
    fotop = models.ImageField(
        upload_to='fotop/', verbose_name='Imagen/Foto perfil')
    nombre = models.CharField(max_length=100, verbose_name='Nombre completo')
    celular = models.CharField(max_length=12, verbose_name='Celular')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    correo = models.CharField(
        max_length=100, verbose_name='Correo electronico')
    pais = models.CharField(max_length=50, verbose_name='Pais')
    contraseña = models.CharField(max_length=15, verbose_name='Contraseña')

    def __str__(self):
        return (self.rut)
