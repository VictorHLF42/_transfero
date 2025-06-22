<<<<<<< HEAD
# from django.shortcuts import render

# from sistema.models import Usuario


# def listarUsuarios(request):
#     usuarios = Usuario.objects.all() 

#     context = {
#         'usuarios': usuarios,
#     }

#     return render(
#         request,
#         'usuarios/listar.html',
#         context,
#     )


=======
from django.shortcuts import render

from sistema.models import Usuario

def listaUsuarios(request):
    usuarios = Usuario.objects.all()


    context = {
        'usuarios': usuarios
    }

    return render(
        request,
        'usuarios/listar.html',
        context,
    )
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
