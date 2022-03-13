from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models

from .base_model import BaseModel
from utils import Util


# Create your model(s) here.
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a user with the given email and password.
        """
        if not email:
            raise ValueError("Users must provide a valid email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a new superuser with the given email and password
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))
        return self.create_user(
            email,
            password,
            **extra_fields,
            otp_code=Util.generate_otp())


class User(
    BaseModel,
    AbstractBaseUser,
    PermissionsMixin
):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        null=False
    )
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=25, unique=True, null=False)
    first_name = models.CharField(max_length=125, null=False)
    last_name = models.CharField(max_length=125, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=255, null=False)
    otp_code = models.CharField(max_length=6, null=False, editable=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space between.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def get_phone_number(self):
        """
        Returns the phone number of the user.
        """
        return self.phone_number

    def get_username(self):
        """
        Returns the username of the user.
        """
        return self.username

    def get_address(self):
        """
        Returns the address of the user.
        """
        return self.address
