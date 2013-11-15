from django.db import models
import datetime
# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, db_index=True, default=datetime.datetime.now())
    updated = models.DateTimeField(
        auto_now=True, db_index=True, default=datetime.datetime.now())

    class Meta:
        abstract = True
