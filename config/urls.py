from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet, CorViewSet, AcessórioViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"cor", CorViewSet)
router.register(r"acessório", AcessórioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]