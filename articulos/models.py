from __future__ import unicode_literals
from django.db import models

# Create your models here.

class TipoItem(models.Model):
    nombre = models.CharField(max_length=200, default='Griferia')

    def __str__(self):
        return self.nombre
    

class Articulo(models.Model):
    codigo = models.IntegerField(default=1)
    nombre_item = models.CharField(max_length=200, default='grifo')
    tipo_item = models.ForeignKey(TipoItem, on_delete=models.PROTECT)
    precio_unitario = models.IntegerField(default=1, blank = True, null = True)
    cantidad_stock = models.IntegerField(default=1, blank = True, null = True)

    def __str__(self):
        return self.codigo
