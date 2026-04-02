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