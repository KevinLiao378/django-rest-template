from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField


class User(AbstractUser):
    email = EmailField("邮箱", unique=True)
    nick_name = CharField("昵称", blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
