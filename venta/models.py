from django.db import models

# Create your models here.
class producto(models.Model):
	nombre = models.CharField(max_length=40)
	categoria = models.CharField(max_length=40)
	marca = models.CharField(max_length=40)
	fecha_v = models.DateField()

class cliente(models.Model):
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=40)
	correo = models.TextField()
	telefono = models.BigIntegerField()
	direccion = models.TextField()
	id_p = models.ForeignKey(producto, on_delete=models.DO_NOTHING)

class vendedor(models.Model):
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=40)
	dni = models.BigIntegerField()