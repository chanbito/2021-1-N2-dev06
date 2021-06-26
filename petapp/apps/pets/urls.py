from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.list_pets, name='list_pets'),
    path('adicionar/<int:id_client>/', views.add_pet, name='add_pet'),
    path('editar/<int:id_pet>/', views.edit_pet, name='edit_pet'),
    path('excluir/<int:id_pet>/', views.delete_pet, name='delete_pet'),
]
