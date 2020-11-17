from django.db import models

# Create your models here.

class Equipamentos(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Equipamento')

    def __str__(self):
        return self.nome
