from django.shortcuts import render

<<<<<<< HEAD
from sistema.models import Filme

# Aqui irão ficar todas as views (controladores) ref ao App sistema
# A função index informa o que vai acontecer quando ela for chamada.

def index(request):
    fotografias = Filme.objects.order_by('data_cadastro').filter(publicado=True)
    return render(
        request,
        'sistema/index.html',
        {"cards": fotografias}
    )



def suporte(request):
    return render(
        request,
        'sistema/suporte.html',
    )



# Função atual
# def index(request):
#     return render(
#         request,
#         'sistema/index.html',
#     )
=======
# aqui irao ficar todas as views (controladores) ref ao sistema
#a função index informa o que vai acontecer quando ela for chamada.

def index(request):
    return render(
        request,
        'sistema/sistema.html',
    )

>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
