from django.contrib import admin

# Register your models here.
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, Perfil, Formacao, Recurso

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "grau", "duracao_anos")
    search_fields = ("nome", "sigla")

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "area_especializacao")
    search_fields = ("nome", "email")

admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Docente, DocenteAdmin)

class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "ano_curricular", "ects")
    search_fields = ("nome", "codigo", "objetivos", "programa") 
    list_filter = ("ano_curricular", "semestre", "licenciatura")    

admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "unidade_curricular", "ano_letivo", "data_inicio", "destaque")
    search_fields = ("titulo",)
    list_filter = ("destaque", "ano_letivo", "unidade_curricular")

admin.site.register(Projeto, ProjetoAdmin) 

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel_dominio", "destaque")
    search_fields = ("nome", "tipo")
    list_filter = ("tipo", "destaque")

admin.site.register(Tecnologia, TecnologiaAdmin)

class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autores", "ano", "rating")
    search_fields = ("titulo", "autores")
    list_filter = ("ano", "rating")

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

class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "instituicao", "tipo", "data_inicio")
    search_fields = ("nome", "instituicao")
    list_filter = ("tipo",)

admin.site.register(Formacao, FormacaoAdmin)

class RecursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "projeto", "tfc")
    search_fields = ("titulo",)

admin.site.register(Recurso, RecursoAdmin)