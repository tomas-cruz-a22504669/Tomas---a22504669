from django.contrib import admin

# Register your models here.
from .models import Licenciatura, Docente, UnidadeCurricular

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "grau", "duracao_anos")
    search_fields = ("nome", "sigla")

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "area_especializacao")
    search_fields = ("nome", "email")

admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Docente, DocenteAdmin)

class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "ano_curricular", "semestre", "licenciatura")
    search_fields = ("nome", "codigo")
    list_filter = ("ano_curricular", "semestre")

admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)