from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.apps.accounts"
    verbose_name = "账号管理"
