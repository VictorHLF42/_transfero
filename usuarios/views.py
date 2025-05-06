from django.shortcuts import render, redirect

from usuarios.forms import UsuarioForm

# Create your views here.

def login(request):
    return render(
        request,
        'login.html'
    )
def criarUsurio(request):
    # Verificar se a requisição será do tipo GET ou POST 
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        #Será criada um objeto Usuario(model) com os dados enviados 
        # post -> sao os campos do forms (nome, sobrenome) preenchidos.
        # files -> contém os arquivos ou e/imagens.
        if form.is_valid(): # Se os dados forem válidos, são salvos no BD.
            form.save()
            return redirect('/usuario/login')

    
    else: 
        # se a requisição for GET, exibir o formulário de cadastro
        form = UsuarioForm()
    return render(
        request,
        'cadastro.html',
        {'form': form}
    )