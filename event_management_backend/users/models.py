from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("organizer", "Organizer"),
        ("user", "User"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")

    def __str__(self):
        return self.user.username


