from django.contrib import admin

# Register your models here.
from .models import Licenciatura, Docente

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "grau", "duracao_anos")
    search_fields = ("nome", "sigla")

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "area_especializacao")
    search_fields = ("nome", "email")

admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Docente, DocenteAdmin)