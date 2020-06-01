from django.conf import settings
from django.db import models

# Create your models here.

from tags.models import Tag

class TagView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.tag.title)
