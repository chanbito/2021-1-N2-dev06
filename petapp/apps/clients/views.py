from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientForm
from .models import Client
# Create your views here.

@login_required(login_url='/employes/login/')
def add_client(request):
    template_name = 'clients/add_client.html'
    context = {}
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('client:list_clients')
    form = ClientForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/employes/login/')
def list_clients(request):
    template_name = 'clients/list_clients.html'
    clients = Client.objects.filter()
    context = {
        'clients': clients,
    }
    return render(request, template_name, context)

@login_required(login_url='/employes/login/')
def edit_client(request, id_client):
    template_name = 'clients/add_client.html'
    context ={}
    client = get_object_or_404(Client, id=id_client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client:list_clients')
    form = ClientForm(instance=client)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/employes/login/')
def delete_client(request, id_client):
    client = Client.objects.get(id=id_client)
    client.delete()
    return redirect('client:list_clients')

@login_required(login_url='/employes/login/')
def search_clients(request):
    template_name = 'clients/list_clients.html'
    query = request.GET.get('query')
    clients = Client.objects.filter(last_name__icontains=query)
    context = {
        'clients': clients
    }
    return render(request,template_name, context)