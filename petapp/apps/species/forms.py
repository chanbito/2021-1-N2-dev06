from django import forms
from .models import Specie

class SpecieForm(forms.ModelForm):
    class Meta:
        model = Specie
        exclude = ()
