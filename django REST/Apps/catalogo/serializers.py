from rest_framework import serializers
from Apps.catalogo.models import CatalogoModelo

class CatalogoSerialize(serializers.ModelSerializer):
    class Meta:
        model = CatalogoModelo
        fields = ['pk', 'codigoProd', 'nombreProd', 'detalleProd', 'precioProd' , 'fechaIngreso' , 'stock']
