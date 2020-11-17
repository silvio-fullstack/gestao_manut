from django.db import models

# Create your models here.
class Almoxarifado(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Peça')
    descricao = models.TextField(help_text='Descrição da Peça')

    def __str__(self):
        return self.nome

