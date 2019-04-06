from __future__ import unicode_literals
from django.contrib import admin
from .models import *

# Register your models here.


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre_item', 'tipo_item', 'precio_unitario', 'cantidad_stock')
    list_editable = ('tipo_item', )

class TipoItemAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', )
    list_editable = ('nombre', )

admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(TipoItem,TipoItemAdmin)
