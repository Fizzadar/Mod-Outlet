# Mod Outlet
# File: apps/users/models.py
# Desc: user model

from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager as DjangoUserManager


class UserManager(DjangoUserManager):
    pass


class User(AbstractBaseUser):
    objects = UserManager()
    uuid = models.CharField(max_length=32, editable=False, unique=True)

    # Used as username
    email = models.CharField(max_length=100, unique=True)
    # For changing/resetting email (like pw reset, confirm FIRST)
    new_email = models.CharField(max_length=100, unique=True, editable=False)
    new_email_key = models.CharField(max_length=32, editable=False)

    # Display name only
    name = models.CharField(max_length=60)

    date_joined = models.DateField()

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def changeEmail(self, new_email):
        # Generate key
        new_email_key = uuid4()

        # Email new email w/ key link

        # Set the key/email
        self.new_email = new_email
        self.new_email_key = new_email_key

    def validateNewEmail(self, key):
        if self.new_email_key != key:
            return False

        self.email = self.new_email
        return True

    def ban(self):
        self.active = False
        self.save()

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid4()

        super(User, self).save(*args, **kwargs)

    # Required for django user model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name