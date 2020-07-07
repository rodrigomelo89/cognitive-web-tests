from django.db import models


class Exame(models.Model):  # modelo do exame
    nome_completo = models.CharField(max_length=100)  # campo pequeno de texto
    idade = models.IntegerField()  # campo de valores númericos
    genero = models.CharField(max_length=100, choices=[('feminino', 'feminino'), ('masculino', 'masculino'),])
    tempo_de_estudo = models.IntegerField()
    resultados = models.TextField()  # campo de texto grande
    nota = models.IntegerField(default=0)
    transcri = models.TextField()
    audioRecorded = models.FileField(upload_to='media/', blank=True)

    def publish(self):
        self.save()
