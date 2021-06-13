from django.urls import path
from . import views

app_name = 'species'

urlpatterns = [
    path('', views.list_species, name='list_species'),
    path('adicionar/', views.add_specie, name='add_specie'),
    path('editar/<int:id_specie>/', views.edit_specie, name='edit_specie'),
    path('excluir/<int:id_specie>/', views.delete_specie, name='delete_specie'),
]