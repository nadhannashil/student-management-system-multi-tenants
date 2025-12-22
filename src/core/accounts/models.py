from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, role="student"):
        if not email:
            raise ValueError("Email is required")

        if not username:
            raise ValueError("Username is required")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=username,
            role=role,
        )

        user.set_password(password)

        if role == "staff":
            user.is_staff = True

        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            role="staff"
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ("staff", "Staff"),
        ("student", "Student"),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="student"
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} ({self.role})"
