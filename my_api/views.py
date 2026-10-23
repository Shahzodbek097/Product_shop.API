from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TalabaViewSet(viewsets.ModelViewSet):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer

