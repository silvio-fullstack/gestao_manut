from django.db import models

# Create your models here.

class Producao(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Operador')

    def __str__(self):
        return self.nome
