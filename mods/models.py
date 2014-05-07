# Mod Outlet
# File: apps/mods/models.py
# Desc: mod models

from django.db import models

from lib.models import UidModelBase
from users.models import User


class Category(UidModelBase):
    pass


class Tag(UidModelBase):
    pass


class Mod(UidModelBase):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, 'tags+')