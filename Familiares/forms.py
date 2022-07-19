from django import forms
from django.forms import ModelForm
from django import forms
from .models import Familiar
class UploadForm(ModelForm):
    nombre = forms.TextInput()
    dni = forms.IntegerField()
    nacimiento = forms.DateInput()
    class Meta:
        model = Familiar
        field = ['nombre', 'dni', 'nacimiento']