from django.db import models

# Create your models here.

class Manutencao(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Manutentor')
    
    def __str__(self):
        return self.nome
