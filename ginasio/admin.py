from django.contrib import admin

# Register your models here.
from .models import Cliente, Aula

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade")
    search_fields = ("nome",)

class AulaAdmin(admin.ModelAdmin):
    list_display = ("nome", "treinador")
    search_fields = ("nome", "treinador")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Aula, AulaAdmin)