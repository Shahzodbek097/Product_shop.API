from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view=get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
        description='E-commarce API',
        terms_of_service='http://www.google.com/policies/terms',
        contact=openapi.Contact(email='shahzod@email.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    #API URLs
    path("api/v1/", include('products.urls')),

    #Swagger sxemasi JSON/YAML sxemasi
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    #Swagger interfeysi
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    #ReDoc interfeysi
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
