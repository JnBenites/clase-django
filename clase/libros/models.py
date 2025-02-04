from django.db import models

# Create your models here.

class autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento= models.DateField()
    def __str__(self):
        return self.nombre

class libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)
    def __str__(self):
            return f"{self.titulo} --- {self.autor}"

