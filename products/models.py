from django.db import models
from django.contrib.auth.models import User
from rest_framework.utils import timezone


class Category(models.Model):
    nomi=models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Product(models.Model):
    nomi=models.CharField(max_length=100)
    izoh=models.TextField()
    narxi=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nomi


class Baho(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='baho')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='baho')
    sharh=models.TextField()
    reyting=models.PositiveIntegerField()
    sana=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.reyting}"


class Chegirma(models.Model):
    product=models.OneToOneField(Product, on_delete=models.CASCADE)
    chegirma_foizi=models.PositiveIntegerField()
    boshlanishi=models.DateTimeField()
    tugashi=models.DateTimeField()

    def is_active(self):
        hozir=timezone.now()
        return self.boshlanishi <= hozir <= self.tugashi

    class Meta:
        unique_together=('product', 'boshlanishi', 'tugashi')


class ProductViewHistory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    korgan_vaqti=models.DateTimeField(auto_now_add=True)
