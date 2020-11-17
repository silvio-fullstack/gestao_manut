from django.contrib import admin
from .models import Tipo_Servico, Setor, Ordem_Servico

# Register your models here.

admin.site.register(Tipo_Servico)
admin.site.register(Setor)
admin.site.register(Ordem_Servico)
