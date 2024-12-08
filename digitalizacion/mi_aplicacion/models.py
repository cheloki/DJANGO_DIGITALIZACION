from django.db import models
from django.core.exceptions import ValidationError

from .validators import validar_extension_imagen

def validar_email_unico(email):
    if Usuario.objects.filter(email=email).exists():
        raise ValidationError(f'El email {email} ya está en uso.')

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True,validators=[validar_email_unico])
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Portaobjeto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, through='PortaobjetoCategoria')

    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    archivo = models.ImageField(upload_to='imagenes/', validators=[validar_extension_imagen])
    descripcion = models.TextField()
    fecha_subida = models.DateField(auto_now_add=True)
    portaobjeto = models.ForeignKey(Portaobjeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.archivo.name

class PortaobjetoCategoria(models.Model):
    portaobjeto = models.ForeignKey(Portaobjeto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('portaobjeto', 'categoria')

