from rest_framework import viewsets
from .serializers import *
from core.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated


class ItemGroupViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ItemGroupSerializer
    queryset = ItemGroup.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
