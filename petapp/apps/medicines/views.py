from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicineForm
from .models import Medicine, User

# Create your views here.

def add_medicine(request):
    template_name = 'medicines/add_medicine.html'
    context = {}
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('medicines:list_medicines')
    form = MedicineForm()
    context['form'] = form
    return render(request, template_name, context)

def list_medicines(request):
    template_name = 'medicines/list_medicines.html'
    medicine = Medicine.objects.filter()
    context = {
        'medicines': medicine
    }
    return render(request, template_name, context)

def edit_medicine(request, id_medicine):
    template_name = 'medicines/add_medicine.html'
    context ={}
    medicine = get_object_or_404(Medicine, id=id_medicine)
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES,  instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicines:list_medicines')
    form = MedicineForm(instance=medicine)
    context['form'] = form
    return render(request, template_name, context)

def delete_medicine(request, id_medicine):
    medicine = Medicine.objects.get(id=id_medicine)
    medicine.delete()
    return redirect('medicines:list_medicines')