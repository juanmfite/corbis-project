from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    Levanta el html principal.

    Retorno:
        html

    """
    articulos = Articulo.objects.all()
    return render(request, 'index.html', locals())