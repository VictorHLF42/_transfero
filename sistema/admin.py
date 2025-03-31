from django.contrib import admin
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