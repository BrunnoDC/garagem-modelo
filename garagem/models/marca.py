from django.db import models


class Marca(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
