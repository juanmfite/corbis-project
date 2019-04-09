from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.addFormulario, name='addFormulario'),
    path('formulario/<int:pk>/edit/', views.formulario_edit, name='formulario_edit'),
    path('askDeleteArticulo/<int:pk>', views.askDeleteArticulo, name='askDeleteArticulo'),
    path('deleteArticulo/<int:pk>', views.deleteArticulo, name='deleteArticulo'),
    path('api/articulos', views.ArticuloList.as_view(), name='ArticuloList'),
    path('api/articulos/<int:pk>', views.ArticuloDetail.as_view(), name='ArticuloDetail'),
]