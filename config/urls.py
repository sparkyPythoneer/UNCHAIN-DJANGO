from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


# Swagger-UI.
schema_view = get_schema_view(
    openapi.Info(
        title="Sparky Pythoneer",
        default_version='v1',
        description="An Endpoint for Available Endpoints",
    ),
    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', schema_view.with_ui(
        'swagger', cache_timeout=0),
        name='schema-swagger-ui'),

]
