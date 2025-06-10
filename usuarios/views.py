from django.shortcuts import render, redirect

from usuarios.forms import CadastroForms, LoginForms, UsuarioForm

from django.contrib.auth.models import User #App responsável por acessar os usuários

from django.contrib import auth #App responsável pela autenticação

from django.contrib import messages #App responsável pela mensagens de retorno para o cliente


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
    

# Classe responsável por cadastrar um novo usuário
def cadastrar(request):
    form = CadastroForms()
    
    if form.is_valid():
        nome=form['nome_cadastro'].value()
        email=form['email'].value()
        senha=form['senha'].value()

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

    return render(request, 'usuarios/cadastrar.html', {'form': form})       


# Classe responsável por enviar e-mail de esqueci a senha
def esqueci(request):
    return render(
        request,
        'usuarios/esqueci_a_senha.html'
    )
    

# Classe responável por realizar o logout
def logout(request):
    auth.logout()
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('usuario/login')
