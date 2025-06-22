from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    estudio = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopse = models.TextField()

    def __str__(self):
        return self.nome
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
