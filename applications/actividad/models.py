from django.db import models

# Create your models here.

class Categoria(models.Model):
    """Model definition for Categoria."""
    descripcion = models.CharField('Descripcion',max_length=500)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):

        return self.descripcion

class Actividad(models.Model):
    """Model definition for Actividad."""

    nombre = models.CharField('Nombre',max_length=50)
    fecha = models.DateField('Fecha')
    participantes = models.IntegerField('Participantes',max_length=None)
    objetivo = models.CharField('Objetivo',max_length=500)
    descripcion = models.CharField('Descripcion',max_length=2000)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='actividad',blank=True,null=True)
    class Meta:
        """Meta definition for Actividad."""

        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.nombre
