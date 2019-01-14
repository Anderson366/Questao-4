from django.contrib import admin

from .models import *

class RevistaInLine(admin.TabularInline):
    model = Revista
    extra = 1

class AdminColecao(admin.ModelAdmin):
    inlines = [RevistaInLine, ]

class AmigoInLine(admin.TabularInline):
    model = Amigo
    extra = 1

class RevistaInLine(admin.TabularInline):
    model = Revista

#class AdminEmprestimo(admin.ModelAdmin):
#     inlines = [AmigoInLine, RevistaInLine]

admin.site.register(Revista)
admin.site.register(Caixa)
admin.site.register(Colecao, AdminColecao)
admin.site.register(Amigo)
#admin.site.register(Emprestimo, AdminEmprestimo)