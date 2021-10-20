from django.urls import path, include
from .views import *

from rest_framework.routers import SimpleRouter, DefaultRouter


router = DefaultRouter()
router.register(r"item-group", ItemGroupViewSet)
router.register(r"item", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
