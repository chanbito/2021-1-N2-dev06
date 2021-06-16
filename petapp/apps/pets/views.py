from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Pets

# Create your views here.

def add_ped(request):
    template_name = 'pets/add_pet.html'
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('pets:list_pets')
    form = ProductForm()
    context['form'] = form
    return render(request, template_name, context)

def list_pets(request):
    template_name = 'pets/list_pets.html'
    products = Pets.objects.filter()
    context = {
        'pets': products
    }
    return render(request, template_name, context)

def edit_pet(request, id_product):
    template_name = 'pets/add_pet.html'
    context ={}
    product = get_object_or_404(Pets, id=id_product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,  instance=product)
        if form.is_valid():
            form.save()
            return redirect('pets:list_pets')
    form = ProductForm(instance=product)
    context['form'] = form
    return render(request, template_name, context)

def delete_pet(request, id_product):
    product = Pets.objects.get(id=id_product)
    product.delete()
    return redirect('pets:list_pets')
