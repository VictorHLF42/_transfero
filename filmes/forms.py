from django import forms
<<<<<<< HEAD
from sistema.models import Filme
=======
from sistema.models import Filme 
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'ano', 'estudio', 'genero', 'sinopse',]