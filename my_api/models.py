from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=200)
    athor=models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Talaba(models.Model):
    ismi=models.CharField(max_length=50)
    familyasi=models.CharField(max_length=50)
    yoshi=models.IntegerField()

    def __str__(self):
        return self.familyasi, self.ismi
