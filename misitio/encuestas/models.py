import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    creacion = models.DateTimeField()

    def fue_publicado_recientemente(self):
        return self.creacion >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.texto_pregunta


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcion
