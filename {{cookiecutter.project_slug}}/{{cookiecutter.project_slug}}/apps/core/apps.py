from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.apps.core"
    verbose_name = "通用管理"
