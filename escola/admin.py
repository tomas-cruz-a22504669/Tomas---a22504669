from django.contrib import admin

# Register your models here.
from .models import Professor, Aluno

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "disciplina")
    search_fields = ("nome",)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "ano")
    search_fields = ("nome",)

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)