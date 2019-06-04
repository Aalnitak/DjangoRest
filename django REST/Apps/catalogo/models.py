from django.db import models

class CatalogoModelo(models.Model):
    codigoProd = models.IntegerField()
    nombreProd = models.CharField(max_length=100)
    detalleProd = models.CharField(max_length=200)
    precioProd = models.IntegerField()
    fechaIngreso = models.DateField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombreProd

