from django.db import models

# Create your models here.
class Receita(models.Model):
    nome = models.CharField(max_length=100)
    dificuldade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome