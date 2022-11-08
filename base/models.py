from django.db import models


# base date model
class DatedModel(models.Model):
    class Meta:
        abstract = True

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


# base status model
class StatusModel(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)
