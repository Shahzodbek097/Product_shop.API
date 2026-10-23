from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet,BookViewSet,TalabaViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'talaba', TalabaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]