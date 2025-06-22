from django.urls import path
from sistema import views

<<<<<<< HEAD
# Informa qual será a rota que irá chamar determinada view(função).
urlpatterns = [
    path('', views.index, name='index'),
    # path('listar/', views.listarUsuarios, name='listarusuarios'),
    path('suporte/', views.suporte, name='suporte'),
]
=======

#informa qual será a rota que ele irá chamaar determinada view(função).
urlpatterns = [
    path('', views.index),
    path('listar/', views.listaUsuarios),
    path('listarfilmes/', views.listarFilmes),
]

>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
