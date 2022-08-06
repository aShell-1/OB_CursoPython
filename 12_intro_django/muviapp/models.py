from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=64)
    fecha_estreno = models.CharField(max_length=4, help_text='Año de estreno')
    duracion = models.TimeField(help_text='hh:mm:ss')
    directores = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=1000, help_text='Sinopsis o resumen de la película')
    imagen = models.URLField(help_text='Enlace de la imagen')
    
    def __str__(self):
        return self.titulo

class Director(models.Model):
    nombre = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=20, null=True)
    imagen = models.URLField()
    peliculas = models.ManyToManyField(Pelicula)

    def __str__(self):
        return self.nombre