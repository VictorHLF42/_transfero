<<<<<<< HEAD
=======
from django.urls import path 


>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
from django.urls import path
from usuarios import views

urlpatterns = [
<<<<<<< HEAD
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('esqueci/', views.esqueci, name='esqueci'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
]
=======
    path('cadastro/', views.criarUsurio, name='criarUsuario'),
    path('login/', views.login, name='login'),
]

# 127.0.0.1:8000/usuario
# 127.0.0.1:8000/usuario/login
# 127.0.0.1:8000/usuario/cadastro
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
