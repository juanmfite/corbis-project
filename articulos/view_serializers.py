from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

@login_required
@api_view(['GET'])
def articulos_list(request, format=None):
    """
    Devuelve todas los articulos.

    Retorno
    -------

    serializer.data: json
            Todas las articulos.  

    """
    if request.method == 'GET':
        articulos = Articulo.objects.all()
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def articulos_detail(request, pk, format=None):
    """
    Devuelve el articulo con el pk especificado.

    Retorno
    -------

    serializer.data: json
            Articulo.  

    """
    if request.method == 'GET':
        articulo = Articulo.objects.get(pk=pk)
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
