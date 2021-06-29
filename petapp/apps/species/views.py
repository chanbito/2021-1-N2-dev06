from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import SpeciesForm
from .models import Species

# Create your views here.

@login_required(login_url='/funcionarios/login/')
def add_specie(request):
    template_name = 'species/add_specie.html'
    context = {}
    if request.method == 'POST':
        form = SpeciesForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('species:list_species')
    form = SpeciesForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/funcionarios/login/')
def list_species(request):
    template_name = 'species/list_species.html'
    species = Species.objects.filter()
    context = {
        'species': species
    }
    return render(request, template_name, context)

@login_required(login_url='/funcionarios/login/')
def edit_specie(request, id_specie):
    template_name = 'species/add_specie.html'
    context ={}
    specie = get_object_or_404(Species, id=id_specie)#, user=request.user)
    if request.method == 'POST':
        form = SpeciesForm(request.POST, instance=specie)
        if form.is_valid():
            form.save()
            return redirect('species:list_species')
    form = SpeciesForm(instance=specie)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/funcionarios/login/')
def delete_specie(request, id_specie):
    specie = Species.objects.get(id=id_specie)
    specie.delete()
    return redirect('species:list_species')
