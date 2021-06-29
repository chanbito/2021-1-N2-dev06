from django import forms
from .models import Service, ServiceItem, Pets, Medicine

class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        exclude = ('employe','pet', 'created_on' , 'updated_on')

class ServiceItemForm(forms.ModelForm):
    
    class Meta:
        model = ServiceItem
        exclude = ('employe','service', 'created_on' , 'updated_on')