from django.contrib import admin

# Register your models here.
from .models import Categoria, Produto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")
    search_fields = ("nome",)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)