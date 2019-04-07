from rest_framework import serializers
from .models import *

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('codigo','nombre_item', 'tipo_item', 'precio_unitario','cantidad_stock')

class TipoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoItem
        fields = ('id','nombre',)