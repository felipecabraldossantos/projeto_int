from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    tipo_usuario = models.BooleanField(default=False)

    whatsapp = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
