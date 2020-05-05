from django.db import models
from django.conf import settings
from django.utils import timezone


class Exams(models.Model):
    paciente = models.CharField(max_length=100)
    idade = models.IntegerField()
    genero = models.CharField(max_length=100)
    tempo_estudo = models.IntegerField()
    # experiments =
    # audio =
    resultados = models.TextField()

    def publish(self):
        self.save()
