from django.contrib import admin
<<<<<<< HEAD

from sistema import models

# Aqui fica o registro do Usuário
# @admin.register(models.Usuario)
# class UsuarioAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nome', 'sobrenome', 'email', 'ativo',)

# Aqui fica o registro do Filme
@admin.register(models.Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano', 'estudio', 'genero',)

# Aqui fica o registro do Gênero
@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
=======
from .models import Usuario, Filme, Genero

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'data_cadastro', 'ativo')

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'estudio', 'data_cadastro', 'genero')

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_cadastro')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Genero, GeneroAdmin)
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
