from django.urls import path
from filmes import views  # Note o nome correto da view

urlpatterns = [
    path('cadastrarfilme/', views.cadastrar_filme, name='cadastrarfilme'),
]