from django.contrib import admin

# Register your models here.
from .models import Receita, Ingrediente

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "dificuldade")
    search_fields = ("nome",)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "quantidade")
    search_fields = ("nome",)

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)