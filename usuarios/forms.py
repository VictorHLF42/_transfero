from django import forms # importação o módlo dos formulários do django.
from sistema.models import Usuario    

class UsuarioForm(forms.ModelForm):
    model = Usuario #define qual é o model que o form representa.
    fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco', 'imagem',] #sâo os campos que serão exibidos no form (HTML)