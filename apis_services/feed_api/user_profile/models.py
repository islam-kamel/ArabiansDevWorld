from django.db import models

"""
Create tables in database for more user information
with relationship with user
"""
from user.models import User


class Name(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    user = models.OneToOneField(
        User, related_name="name", primary_key=True, on_delete=models.CASCADE
    )

    class Meta:
        indexes = [
            models.Index(fields=["user_id"]),
        ]

    def __str__(self):
        return self.first_name

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
