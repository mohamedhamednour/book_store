from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    first_name = models.CharField(("first name"), max_length=150)
    last_name = models.CharField(("last name"), max_length=150)
    email = models.EmailField(verbose_name=("email address"), unique=True, null=True)
    username = models.CharField(("Username"), max_length=150, null=True, blank=True)
    phone_number = models.CharField(
        ("Phone number"), max_length=50, unique=True, null=True
    )
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.email}"
