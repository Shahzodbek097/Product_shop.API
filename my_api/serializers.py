from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields="__all__"


class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Talaba
        fields='__all__'
