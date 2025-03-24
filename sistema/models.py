from django.utils import timezone
from django.db import models

class Usuario(models.Model):  # Corrigido: "models.Model"
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)  # Corrigido: removido "models" extra
    # foto = models.ImageField(upload_to='usuarios/')  # Campo opcional (descomente se quiser usar)
