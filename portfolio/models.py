from django.db import models

# Create your models here.
from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    grau = models.CharField(max_length=50)
    duracao_anos = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField()
    saida_profissional = models.TextField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pagina_pessoal_url = models.URLField(blank=True, null=True)
    fotografia = models.ImageField(upload_to='docentes/')
    area_especializacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    semestre = models.IntegerField()
    ano_curricular = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/')
    
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente)

    def __str__(self):
        return self.nome    

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True) # Pode ainda não ter acabado
    imagem = models.ImageField(upload_to='projetos/')
    video_demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    destaque = models.BooleanField(default=False)
    
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50) 
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias/')
    website_oficial = models.URLField(blank=True, null=True)
    nivel_dominio = models.IntegerField()
    nivel_interesse = models.IntegerField()
    destaque = models.BooleanField(default=False)
    
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    resumo = models.TextField()
    area = models.CharField(max_length=100)
    interesse = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    orientador = models.CharField(max_length=100)
    
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo