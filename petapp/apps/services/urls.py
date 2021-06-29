from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.list_services, name='list_services'),
    path('adicionar/<int:id_pet>/', views.add_service, name='add_service'),
    path('excluir/<int:id_service>/', views.delete_service, name='delete_service'),
    path('excluir-item/<int:id_service_item>/', views.delete_service_item, name='delete_service_item'),
    path('adicionar-item/<int:id_service>/', views.add_service_item, name='add_service_item'),
]