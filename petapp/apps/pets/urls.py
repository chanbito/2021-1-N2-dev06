from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.list_clients, name='list_pets'),
    path('adicionar/', views.add_client, name='add_pet'),
    path('editar/<int:id_pet>/', views.edit_client, name='edit_pet'),
    path('excluir/<int:id_pet>/', views.delete_client, name='delete_pet'),
]
