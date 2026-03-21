from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    ano = models.IntegerField()

    def __str__(self):
        return self.nome