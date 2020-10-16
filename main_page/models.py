from django.db import models
from django.contrib.auth import models as auth_models

# Source for learning more about models: https://docs.djangoproject.com/en/3.1/topics/db/models/


class Issue(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def id_name(self):
        """ Returns a version of the name used for HTML id tags"""
        return self.name.lower().replace(' ', '-')
    
    def has_resources(self):
        """ Checks if the issue has any active resources attached to it"""
        for resource in self.resource_set.all():
            if resource.status == 'A':
                return True
        return False


class Resource(models.Model):
    STATUS_CHOICES = [
        ('R', 'Rejected'),
        ('P', 'Pending Approval'),
        ('A', 'Approved')
    ]
    title = models.CharField(max_length=75)
    url = models.CharField(max_length=100)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    submitter = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def active(self):
        """ Checks if the resource has been approved """
        return self.status == 'A'

    def user_resource(self):
        """ Checks if the resource was submitted by a site user (rather than an admin) """
        return self.submitter.is_staff
