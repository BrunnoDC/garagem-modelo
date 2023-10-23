from django.db import models

from models.categoria import Categoria
from models.marca import Marca


class Modelo(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="modelos"
    )
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelos")
    nome = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.marca} ({self.nome})"

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
