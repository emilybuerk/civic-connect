# Create your models here.
from django.db import models


class Template(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

    def template_title(self):
        """ Returns a version of the name used for HTML id tags"""
        return self.title

    def template_body(self):
        """ Returns the templates body"""
        return self.body