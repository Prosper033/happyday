from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
import uuid

# Create your models here.


class Person(AbstractBaseUser):
    id = models.UUIDField("Person unique id", primary_key=True, default=uuid.uuid4(), null=False)
    last_name = models.CharField("Person last name", max_length=50, null=False, blank=False)
    first_name = models.CharField("Person first name", max_length=50, null=True, blank=True)
    email = models.EmailField("Person email", null=False, unique=True, blank=False)
    password = models.CharField("Person password", max_length=150, null=False, blank=False)
    address = models.CharField("Person address", max_length=150, null=False, blank=False)
    telephone = models.CharField("Person phone number", max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    role = models.ManyToManyField("Role")
    permission = models.ManyToManyField("Permission")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["email", "password"]


class Role(models.Model):
    id = models.UUIDField("Role id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Role name", max_length=20, null=False, blank=False, unique=True)
    description = models.CharField("Role description", max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    permission = models.ManyToManyField("Permission")


class Permission(models.Model):
    id = models.UUIDField("Permission id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Permission name", unique=True, null=False, blank=False, max_length=20)
    description = models.CharField("Permission description", null=False, blank=False, max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
