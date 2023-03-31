from django.contrib import admin
from garagem.models import Marca, Acessório, Cor, Categoria, Veiculo

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessório)
admin.site.register(Cor)
admin.site.register(Veiculo)