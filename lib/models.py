from uuid import uuid4
from django.db import models

class UidModelBase(models.Model):
    uuid = models.CharField(max_length=32, editable=False, unique=True)
    name = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid4()

        super(UidModelBase, self).save(*args, **kwargs)