
from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag
# Create your models here.

my_item = [('computer','science'),('programming','java'),('hardware','cpu')]

class Todo(models.Model):

    name = models.CharField(max_length=220)
    description = models.CharField(max_length=520)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, related_name='%(class)s_requests_created')
