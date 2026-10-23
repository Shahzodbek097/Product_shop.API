from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ProductSerializers(serializers.ModelSerializer):
    orta_reyting=serializers.FloatField(read_only=True, required=False)

    class Meta:
        model=Product
        fields=['id', 'nomi', 'narxi', 'izoh', 'category', 'orta_reyting']


class BahoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Baho
        fields='__all__'


class ProductHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductViewHistory
        fields='__all__'
