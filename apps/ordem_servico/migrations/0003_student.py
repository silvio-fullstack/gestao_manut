# Generated by Django 3.1.3 on 2020-11-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordem_servico', '0002_auto_20201117_0318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2)),
            ],
        ),
    ]