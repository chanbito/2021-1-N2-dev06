from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServiceForm, ServiceItemForm
from .models import Service, ServiceItem, Medicine, Pets
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/employes/login/')
def add_service(request, id_pet):
    template_name = 'services/add_service.html'
    context = {}
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.pet = Pets.objects.get(id=id_pet)
            f.employe = request.user
            f.save()
            form.save_m2m()
            return redirect('services:list_services')
    form = ServiceForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/employes/login/')
def list_services(request):
    template_name = 'services/list_services.html'
    services = Service.objects.filter(employe_id=request.user)
    service_items = ServiceItem.objects.filter()
    medicine = Medicine.objects.filter()
    pet = Pets.objects.filter()
    context = {
        'services': services,
        'service_items': service_items,
        'medicines':medicine,
        'pets': pet
    }
    return render(request, template_name, context)

@login_required(login_url='/employes/login/')
def delete_service(request, id_service):
    order = Service.objects.get(id=id_service)
    order.delete()
    return redirect('services:list_services')

@login_required(login_url='/employes/login/')
def add_service_item(request, id_service):
    template_name = 'services/add_service_item.html'
    context = {}
    if request.method == 'POST':
        form = ServiceItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.service = Service.objects.get(id=id_service)
            f.user = request.user            
            f.save()
            form.save_m2m()
            return redirect('services:list_services')
    form = ServiceItemForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/employes/login/')
def delete_service_item(request, id_service_item):
    serviceitem = ServiceItem.objects.get(id=id_service_item)
    serviceitem.delete()
    return redirect('services:list_services')