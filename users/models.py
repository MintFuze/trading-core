from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = "user", "Пользователь"
        ANALYST = "analyst", "Аналитик"
        ADMIN = "admin", "Администратор"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )

    balance = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0,
    )
