from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def askDeleteArticulo(request,pk):
    articulo = Articulo.objects.get(pk=pk)
    return render(request, 'askDelete.html', locals())

@login_required
def deleteArticulo(request,pk):
    Articulo.objects.filter(pk=pk).delete()
    return render(request, 'delete.html')

@login_required
def addFormulario(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    if request.method == "GET":
        form = ArticuloForm()
    return render(request, 'formAdd.html', {'form': form})

@login_required
def formulario_edit(request,pk):

    articulo = Articulo.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.save()
            return redirect('index', pk=post.pk)
    else:
        form = ArticuloForm(instance=articulo)

    return render(request, 'formEdit.html', {'form': form})