from django.db import models

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    motor = models.CharField(max_length=50)
    cilindros = models.CharField(max_length=50)
    valvulas = models.CharField(max_length=20)
    potencia = models.CharField(max_length=50)
    kilometraje= models.IntegerField()
    año = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='generator/images/', null=True)
    fecha_publicacion =  models.DateTimeField(auto_now_add=True)
    num_puertas = models.IntegerField()
    class Meta:
        db_table = 'Carro'

class ImagenCarro(models.Model):
    carro = models.ForeignKey(Carro, related_name='imagenes', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='generator/images/', null=True)

