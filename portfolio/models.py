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
    objetivos = models.TextField(blank=True, null=True)
    programa = models.TextField(blank=True, null=True)
    avaliacao = models.TextField(blank=True, null=True)
    
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente)

    def __str__(self):
        return self.nome    

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True) 
    imagem = models.ImageField(upload_to='projetos/')
    video_demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    destaque = models.BooleanField(default=False)
    ano_letivo = models.CharField(max_length=20, blank=True, null=True) 
    
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
    autores = models.CharField(max_length=200)
    orientadores = models.CharField(max_length=200)
    licenciaturas = models.CharField(max_length=200)
    ano = models.CharField(max_length=20)
    sumario = models.TextField()
    pdf_link = models.URLField(blank=True, null=True, max_length=500)
    imagem = models.CharField(max_length=200, blank=True, null=True)
    rating = models.IntegerField(default=0)
    
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.CharField(max_length=50) 
    tipo = models.CharField(max_length=50)
    evidencia = models.CharField(max_length=200, blank=True, null=True) # Pode ser um link ou texto
    
    # Relacionamentos (N:M)
    projetos = models.ManyToManyField(Projeto, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to='perfil/')
    email = models.EmailField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    objetivo_profissional = models.TextField()

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField()
    certificado_url = models.URLField(blank=True, null=True)
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    competencias = models.ManyToManyField(Competencia, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.instituicao}"

class Recurso(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50) 
    url = models.URLField()
    descricao = models.TextField(blank=True, null=True)
    
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True, blank=True)
    tfc = models.ForeignKey(TFC, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo