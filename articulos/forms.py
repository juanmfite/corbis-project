from django import forms

from .models import *

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ('codigo', 'nombre_item', 'tipo_item', 'precio_unitario', 'cantidad_stock')