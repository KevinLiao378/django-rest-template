from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# API 文档设置
schema_view = get_schema_view(
   openapi.Info(
      title="{{ cookiecutter.project_slug }} APIs",
      default_version="v{{ cookiecutter.version }}",
      description="{{ cookiecutter.description }}",
      contact=openapi.Contact(email="{{cookiecutter.email}}"),
      license=openapi.License(name="MIT License"),
   ),
   public=False,
   permission_classes=[permissions.AllowAny],
)
