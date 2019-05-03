from django.urls import path, include
from rest_framework import routers

from . import views

# Define router as a default router
# All get, post, delete, put, patch methods for REST
router = routers.DefaultRouter()

# Register each routers for a viewset
router.register(r'biljnevrste', views.BiljnaVrstaViewSet)
router.register(r'podvrste', views.PodvrstaViewSet)
router.register(r'porodice', views.PorodicaViewSet)
router.register(r'rodovi', views.RodViewSet)
router.register(r'sistematicari', views.SistematicarViewSet)
router.register(r'slike', views.SlikaViewSet)
router.register(r'uporabnidijelovi', views.UporabniDioViewSet)
router.register(r'varijeti', views.VarijetViewSet)

urlpatterns = [
    path('', include(router.urls))
]