from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None  # type: ignore
    last_name = None  # type: ignore
