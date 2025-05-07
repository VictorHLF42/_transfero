from django import forms
from .models import Filme  # Agora esse import funcionará

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'