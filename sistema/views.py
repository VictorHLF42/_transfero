from django.shortcuts import render

# aqui irao ficar todas as views (controladores) ref ao sistema


def index(request):
    return render(
        request,
        'sistema/index.html',
    )



