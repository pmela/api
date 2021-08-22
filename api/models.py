from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=64)
    nascimento = models.DateField()
    filiacao = models.CharField(max_length=64)
    residencia = models.CharField(max_length=64)
