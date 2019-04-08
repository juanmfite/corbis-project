from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.addFormulario, name='addFormulario'),
    path('formulario/<int:pk>/edit/', views.formulario_edit, name='formulario_edit'),
    path('askDeleteArticulo/<int:pk>', views.askDeleteArticulo, name='askDeleteArticulo'),
    path('deleteArticulo/<int:pk>', views.deleteArticulo, name='deleteArticulo'),
    path('api/articulos', views.articulos_list, name='articulos_list'),
    path('api/articulos/<int:pk>', views.articulos_detail, name='articulos_detail'),
]