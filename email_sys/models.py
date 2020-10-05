from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone


class Template(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    def __str__(self):
        return self.title
