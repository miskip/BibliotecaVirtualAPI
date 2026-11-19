from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}".strip()


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    isbn = models.CharField(max_length=20, unique=True, null=True, blank=True)
    codigo_interno = models.CharField(max_length=30, unique=True, null=True, blank=True)
    titulo = models.CharField(max_length=20)
    autores = models.ManyToManyField(Autor, related_name='libros')
    categorias = models.ManyToManyField(Categoria, related_name='libros', blank=True)
    archivo = models.FileField(upload_to='libros/')
    formato = models.CharField(max_length=10)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    fecha_publicacion = models.PositiveIntegerField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
