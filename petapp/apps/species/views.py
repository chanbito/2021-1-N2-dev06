from django.shortcuts import render, get_object_or_404, redirect

from .forms import SpecieForm
from .models import Specie

# Create your views here.

def add_specie(request):
    template_name = 'Species/add_specie.html'
    context = {}
    if request.method == 'POST':
        form = SpecieForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('species:list_species')
    form = SpecieForm()
    context['form'] = form
    return render(request, template_name, context)

def list_species(request):
    template_name = 'species/list_species.html'
    species = Specie.objects.filter(user=request.user)
    context = {
        'species': species
    }
    return render(request, template_name, context)

def edit_specie(request, id_specie):
    template_name = 'species/add_species.html'
    context ={}
    specie = get_object_or_404(Specie, id=id_specie, user=request.user)
    if request.method == 'POST':
        form = SpecieForm(request.POST, instance=specie)
        if form.is_valid():
            form.save()
            return redirect('species:list_species')
    form = SpecieForm(instance=specie)
    context['form'] = form
    return render(request, template_name, context)

def delete_specie(request, id_specie):
    specie = Specie.objects.get(id=id_specie)
    if specie.user == request.user:
        specie.delete()
    else:
        return redirect('core:home')
    return redirect('species:list_species')
