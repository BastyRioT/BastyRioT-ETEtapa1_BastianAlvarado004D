# Generated by Django 3.2.3 on 2021-07-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='celular',
            field=models.CharField(max_length=12, verbose_name='celular'),
        ),
    ]
