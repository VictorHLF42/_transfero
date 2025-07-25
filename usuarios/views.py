from django.shortcuts import render, redirect

<<<<<<< HEAD
from usuarios.forms import CadastroForms, LoginForms

from django.contrib.auth.models import User #App responsável por acessar os usuários

from django.contrib import auth #App responsável pela autenticação

from django.contrib import messages #App responsável pela mensagens de retorno para o cliente
from django.contrib.auth import logout as auth_logout


# Classe referente as informações da autenticação
def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form}) 


# Classe responsável por enviar e-mail de esqueci a senha
def esqueci(request):
    return render(
        request,
        'usuarios/esqueci_a_senha.html'
    )
    

# Classe responável por realizar o logout
def logout(request):
    auth_logout(request)
    return redirect('login')

def cadastrar(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastrar')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')
    else:
        form = CadastroForms()

    return render(request, 'usuarios/cadastrar.html', {'form': form})

def perfil(request):
    return render(
        request,
        'usuarios/perfil.html'
=======
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
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
    )