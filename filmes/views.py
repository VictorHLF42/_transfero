from django.shortcuts import render, redirect
from .forms import FilmeForm  

def cadastrar_filme(request):  
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes') 
    else:
        form = FilmeForm()
    return render(request, 'filmes/cadastrar.html', {'form': form})
