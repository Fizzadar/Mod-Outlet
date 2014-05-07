# Mod Outlet
# File: apps/files/models.py
# Desc: file models

from django.db import models

from lib.models import UidModelBase


class BaseFile(UidModelBase):
    file_name = models.CharField(max_length=128, editable=False)
    file_extension = models.CharField(max_length=5, editable=False)


class ImageFile(BaseFile):
    pass


class ModFile(BaseFile):
    pass