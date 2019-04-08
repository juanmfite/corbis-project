from django import forms
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ('codigo', 'nombre_item', 'tipo_item', 'precio_unitario', 'cantidad_stock')