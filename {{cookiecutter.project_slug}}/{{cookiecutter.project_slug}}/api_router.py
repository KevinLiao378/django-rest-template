from django.urls import re_path, include, path
from .docs import schema_view

app_name = "api"

urlpatterns = [
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('users/', include('{{ cookiecutter.project_slug }}.apps.accounts.urls')),
]
