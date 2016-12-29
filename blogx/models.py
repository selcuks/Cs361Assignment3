from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag
# Create your models here.

class blogxx(models.Model):

    name_s = models.CharField(max_length=220)
    description_s = models.CharField(max_length=520)
    owner_s = models.ForeignKey(User)
    tags_s = models.ManyToManyField(Tag)