# Generated by Django 4.2.4 on 2023-08-15 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Acessorio",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Acessorio",
                "verbose_name_plural": "Acessorios",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.CreateModel(
            name="Cor",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Cor",
                "verbose_name_plural": "Cores",
            },
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Marca",
                "verbose_name_plural": "Marcas",
            },
        ),
        migrations.CreateModel(
            name="Modelo",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="modelos",
                        to="models.categoria",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="modelos",
                        to="models.marca",
                    ),
                ),
            ],
            options={
                "verbose_name": "Modelo",
                "verbose_name_plural": "Modelos",
            },
        ),
        migrations.CreateModel(
            name="Veiculo",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("ano", models.IntegerField(blank=True, null=True)),
                ("descricao", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "cor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="models.cor",
                    ),
                ),
                (
                    "modelo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="models.modelo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Veiculo",
                "verbose_name_plural": "Veiculos",
            },
        ),
    ]
