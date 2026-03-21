from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Aula(models.Model):
    nome = models.CharField(max_length=100)
    treinador = models.CharField(max_length=100)

    def __str__(self):
        return self.nome