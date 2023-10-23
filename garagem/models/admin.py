from django.contrib import admin

from models.acessorio import Acessorio
from models.categoria import Categoria
from models.cor import Cor
from models.marca import Marca
from models.modelo import Modelo
from models.veiculo import Veiculo

admin.site.register(Veiculo)
admin.site.register(Modelo)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Acessorio)
admin.site.register(Marca)
