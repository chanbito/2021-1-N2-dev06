"""petapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('especies/', include('species.urls', namespace='species')),
    path('funcionarios/', include('employes.urls', namespace='employes')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('pets/', include('pets.urls', namespace='pets')),
    path('servico/',include('services.urls', namespace='services')),
    path('medicamento/', include('medicines.urls', namespace='medicines')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)