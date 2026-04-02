from django.contrib import admin

# Register your models here.
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, Perfil

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

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "unidade_curricular", "data_inicio", "destaque")
    search_fields = ("titulo",)
    list_filter = ("destaque", "unidade_curricular")

admin.site.register(Projeto, ProjetoAdmin) 

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel_dominio", "destaque")
    search_fields = ("nome", "tipo")
    list_filter = ("tipo", "destaque")

admin.site.register(Tecnologia, TecnologiaAdmin)

class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "area")
    search_fields = ("titulo", "autor")
    list_filter = ("ano", "area")

admin.site.register(TFC, TFCAdmin)

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel")
    search_fields = ("nome",)
    list_filter = ("tipo", "nivel")

admin.site.register(Competencia, CompetenciaAdmin)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome",)

admin.site.register(Perfil, PerfilAdmin)