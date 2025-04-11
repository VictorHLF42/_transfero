from django.shortcuts import render
from sistema.models import Filme  # Certifique-se de importar o modelo Filme

def listarFilmes(request):
    # Busca todos os filmes no banco de dados
    filmes = Filme.objects.all()
    
    # Cria o dicionário de contexto
    context = {
        'filmes': filmes
    }
    
    # Renderiza o template com os dados
    return render(request, 'filmes/listar_filmes.html', context)