from django.shortcuts import render

# aqui irao ficar todas as views (controladores) ref ao sistema
#a função index informa o que vai acontecer quando ela for chamada.

def index(request):
    return render(
        request,
        'sistema/sistema.html',
    )
def indexApresentacao(request):
    return render(
        request,
        'sistema/apresentacao.html',
    )


