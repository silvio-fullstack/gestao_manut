# Generated by Django 3.1.3 on 2020-11-17 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordem_servico', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Setor',
        ),
        migrations.DeleteModel(
            name='Tipo_Servico',
        ),
    ]