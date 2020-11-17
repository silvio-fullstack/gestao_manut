from django.db import models

# Create your models here.

class Tipo_Servico(models.Model):
    tipo = models.CharField(max_length=100, help_text='Tipo do Serviço')
    descricao = models.TextField(help_text='Descrição do Tipo de Serviço')

    def __str__(self):
        return self.tipo

class Setor(models.Model):
    setor = models.CharField(max_length=100, help_text='Nome do Setor da Empresa')
    centro_custo = models.CharField(max_length=100, help_text='Centro de custo do Setor')

    def __str__(self):
        return self.setor


class Ordem_Servico(models.Model):
    causa = models.TextField(help_text='Causa do ProBlema')
    realizado = models.TextField(help_text='Serviço Realizado')

    def __str__(self):
        return self.causa


