# Create your models here.
from django.db import models
import re


template_parameter = re.compile(r'\[([^\[\]]*)\]')


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

    def get_parameters(self):
        """ Returns a list of all the parameters used in the template """
        params = []
        for match in template_parameter.finditer(str(self.body)):
            if match.group(1) not in params:
                params.append(match.group(1))
        return params
