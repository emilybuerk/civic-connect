from django.db import models
from django.contrib.auth import models as auth_models

# Source for learning more about models: https://docs.djangoproject.com/en/3.1/topics/db/models/


class Issue(models.Model):
    name = models.CharField(max_length=40)


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
