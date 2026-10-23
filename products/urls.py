from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *
from .service.chegirma import ChegirmaListCreateView, chegirmada
from .service.product_history import ProductViewHistoryCreate, ProductHistory_list

router = DefaultRouter()
router.register(r"kategoriyalar", CategoryViewSet)
router.register(r'productlar', ProductViewSet)
router.register(r'baholar', BahoViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path('chegirma/', ChegirmaListCreateView.as_view(), name='sale'),
    path('chegirmada/<int:product_id>/', chegirmada, name='product-history-create'),
    path("ko'rilgan/", ProductViewHistoryCreate.as_view(), name="product-history-create"),
    path("jami_ko'rilgan/", ProductHistory_list, name="product-history-list")
]
