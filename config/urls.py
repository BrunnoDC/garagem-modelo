from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet, CorViewSet, AcessórioViewSet, ModeloViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"cor", CorViewSet)
router.register(r"acessório", AcessórioViewSet)
router.register(r"modelo", ModeloViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]