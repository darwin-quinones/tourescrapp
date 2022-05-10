from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=250)
    lugar_recidencia = models.CharField(max_length=60)
    genero = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    identificacion = models.IntegerField()
    tipo_identificacion = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=20)

    def __str__(self):
        fila = 'persona: ' + self.nombres + ' - ' + 'email: ' + self.email
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