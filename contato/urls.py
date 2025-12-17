from django.urls import path
from contato.views import index, listar, adicionar, editar, apagar

urlpatterns = [
    path('', index),
    path('listar/', listar, name='listar'),
    path('novo/', adicionar, name='adicionar'),
    path('editar/<int:numero>', editar, name='editar'),
    path('apagar/<int:numero>', apagar, name='apagar'),
]