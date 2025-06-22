from django.urls import path
<<<<<<< HEAD
from filmes import views

urlpatterns = [
    path('cadastrar/', views.cadastrarFilme, name='cadastrarfilme'),
    path('listar/', views.listarFilmes, name='listarfilmes'),
    path('filmes/', views.filmes, name='filmes'),
    path('imagem/<int:foto_id>', views.imagem, name='imagem'),
    path('buscar', views.buscar, name='buscar'),
    # path('detalhes/', views.detalhes, name='detalhes'),
]


=======
from filmes import views  # Note o nome correto da view

urlpatterns = [
    path('cadastrarfilme/', views.cadastrarFilme),
]
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
