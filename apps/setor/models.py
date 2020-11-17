from django.db import models

# Create your models here.

class Setor(models.Model):
    setor = models.CharField(max_length=100, help_text='Nome do Setor')


    def __str__(self):
        return self.setor
