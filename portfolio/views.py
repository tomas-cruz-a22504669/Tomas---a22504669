from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tecnologia, Competencia, Formacao
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos') 
    
    return render(request, 'portfolio/projeto_form.html', {'form': form})

def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
        
    return render(request, 'portfolio/projeto_form.html', {'form': form})

def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
        
    return render(request, 'portfolio/projeto_apaga.html', {'projeto': projeto})

    def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_form.html', {'form': form})

def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_form.html', {'form': form})

def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_apaga.html', {'tecnologia': tecnologia})

def competencias_view(request):
    return render(request, 'portfolio/competencias.html', {'competencias': Competencia.objects.all()})

def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_form.html', {'form': form})

def edita_competencia_view(request, competencia_id):
    obj = get_object_or_404(Competencia, id=competencia_id)
    form = CompetenciaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_form.html', {'form': form})

def apaga_competencia_view(request, competencia_id):
    obj = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_apaga.html', {'obj': obj})

def formacoes_view(request):
    return render(request, 'portfolio/formacoes.html', {'formacoes': Formacao.objects.all()})

def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html', {'form': form})

def edita_formacao_view(request, formacao_id):
    obj = get_object_or_404(Formacao, id=formacao_id)
    form = FormacaoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html', {'form': form})

def apaga_formacao_view(request, formacao_id):
    obj = get_object_or_404(Formacao, id=formacao_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_apaga.html', {'obj': obj})

def sobre_view(request):
    return render(request, 'portfolio/sobre.html')    