from django.shortcuts import render
from .models import Curso, Professor, Aluno

def cursos_view(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'curso/cursos.html', {'cursos': cursos})

def professores_view(request):
    # Vai buscar os professores e 'pré-carrega' os cursos de cada um para ser eficiente
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'curso/professores.html', {'professores': professores})

def alunos_view(request):
    # Vai buscar os alunos e 'pré-carrega' os cursos de cada um
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'curso/alunos.html', {'alunos': alunos})