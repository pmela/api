from django.db import models


class Nota(models.Model):
    materia = models.CharField(max_length=16)
    nota = models.PositiveIntegerField()

    def __str__(self):
        return self.materia + ' ->  ' + str(self.nota)


class Aluno(models.Model):
    nome = models.CharField(max_length=64)
    nascimento = models.DateField()
    filiacao = models.CharField(max_length=64)
    residencia = models.CharField(max_length=64)
    notas = models.ManyToManyField(Nota, blank=True, null=True)

    def __str__(self):
        return self.nome
