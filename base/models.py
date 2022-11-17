from django.db import models


# base date model
class DatedModel(models.Model):
    """Abstract model that that auto add date_created and date_modified to the objects"""

    class Meta:
        abstract = True

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


# base status model
class StatusModel(models.Model):
    """Abstract model that that auto add is_active to the objects"""

    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)


class ActiveObjectManager(models.Manager):
    """Generic model manager that fetches only the objects with is_active=True"""

    def get_queryset(self):
        return super(ActiveObjectManager, self).get_queryset().filter(is_active=True).order_by('id')
