from django import forms
from module_cours.models import Cours

class CoursForm(forms.ModelForm):
  nom = forms.CharField(label='Nom', max_length=100)
  class Meta:
    model = Cours
    fields = '__all__'