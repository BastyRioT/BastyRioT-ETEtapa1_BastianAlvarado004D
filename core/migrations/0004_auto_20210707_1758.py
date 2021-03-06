# Generated by Django 3.2.3 on 2021-07-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_colaborador_fotop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='celular',
            field=models.CharField(max_length=12, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='contraseña',
            field=models.CharField(max_length=15, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='correo',
            field=models.CharField(max_length=100, verbose_name='Correo electronico'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='direccion',
            field=models.CharField(max_length=100, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='fotop',
            field=models.ImageField(upload_to='fotop/', verbose_name='Imagen/Foto perfil'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre completo'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='pais',
            field=models.CharField(max_length=50, verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut colaborador'),
        ),
    ]
