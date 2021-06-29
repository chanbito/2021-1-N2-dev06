from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('', views.list_medicines, name='list_medicines'),
    path('adicionar/', views.add_medicine, name='add_medicine'),
    path('editar/<int:id_medicine>/', views.edit_medicine, name='edit_medicine'),
    path('excluir/<int:id_medicine>/', views.delete_medicine, name='delete_medicine'),
]