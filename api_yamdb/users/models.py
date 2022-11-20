from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель User."""

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin'),
    ]
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user')
    confirmation_code = models.CharField(blank=True, null=True, max_length=150)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('username',)

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    def __str__(self):
        return self.username
