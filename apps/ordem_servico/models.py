from django.db import models

# Create your models here.


class Ordem_Servico(models.Model):
    causa = models.TextField(help_text='Causa do ProBlema')
    realizado = models.TextField(help_text='Serviço Realizado')

    def __str__(self):
        return self.causa
        