# Users model

#Django
from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lugar_recidencia = models.CharField(max_length=60)
    genero = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    identificacion = models.IntegerField()
    tipo_identificacion = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=20)
    picture = models.ImageField(
        upload_to = 'imagenes/',
        blank = True, 
        null = True
    )

    def __str__(self):
        fila = 'persona: ' + self.user.username + ' - ' + 'email: ' + self.user.email + ' - '+ ' identificacion '+ self.tipo_identificacion + ' - '+ ' fecha_nacimiento '+ self.fecha_nacimiento + ' - '+ ' lugar_recidencia '+ self.lugar_recidencia
        return fila
    
class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name="imagen")
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length= 50)
    puntaje = models.CharField(max_length= 50)
    status = models.IntegerField()

    def __str__(self):
        fila = 'hotel ' + self.nombre + ' - ' + 'puntaje: ' + self.puntaje
        return fila
    
    # funcion para eliminar la foto 
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()