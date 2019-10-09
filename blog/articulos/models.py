from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField


class Articulo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    cuerpo = HTMLField()
    mostrar = models.BooleanField(default=True)
    creacion = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo + ' (' + self.autor.username + ')' + ' - fecha: ' + self.creacion.strftime('%d-%m-%Y %H:%M:%S')


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    cuerpo = models.TextField()
    mostrar = models.BooleanField(default=True)
    creacion = models.DateTimeField(default=timezone.now)
