from django.db import models
from django.contrib.auth import models as auth_models

import requests

# Source for learning more about models: https://docs.djangoproject.com/en/3.1/topics/db/models/

# Parameters for Google Civic Information API query
CIVIC_INFO_API_PARAMS = {
            'key': 'AIzaSyAzUsEsBZFnqSlDtBn6YZJsP-wfpRiQHkc',
            'levels': ['administrativeArea1', 'country'],
            'roles': ['headOfGovernment', 'legislatorUpperBody', 'legislatorLowerBody']
        }


def format_address(address):
    """ Takes an address dictionary retrieved from the Google Civic Information API and returns a string formatted
    for mailing to that address. """
    return address['line1'] \
           + '\n' + address['city'] \
           + ', ' + address['state'] \
           + ' ' + address['zip']


class Official:
    def __init__(self, name, off, address):
        self.name = name
        self.office = off
        self.address = address
        self.email = False
        self.photo = False

    def __str__(self):
        return self.name + ' (' + self.office + ')'

    def get_address(self):
        return self.name + '\n' + format_address(self.address)

    def get_address_lines(self):
        return self.get_address().split('\n')


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

    def active_resources(self):
        """ Returns a list of all the resources that are currently active """
        resources = []
        for resource in self.resource_set.all():
            if resource.active():
                resources.append(resource)
        resources.sort(key=lambda x: x.title)
        return resources


class Resource(models.Model):
    STATUS_CHOICES = [
        ('R', 'Rejected'),
        ('P', 'Pending Approval'),
        ('A', 'Approved')
    ]
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=1000)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    submitter = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def active(self):
        """ Checks if the resource has been approved """
        return self.status == 'A'

    def user_resource(self):
        """ Checks if the resource was submitted by a site user (rather than an admin) """
        return not self.submitter.is_staff

    def get_submitter(self):
        """ Returns either the username of the submitter or 'Anonymous User' 
        depending on the submitter's preferences """
        if self.anonymous:
            return 'Anonymous User'
        return self.submitter.username


def government_officials(address):
    """ Returns a 2D list of the government officials presiding over the given address separated by government level """
    query_params = CIVIC_INFO_API_PARAMS
    query_params['address'] = address
    response = requests.get('https://www.googleapis.com/civicinfo/v2/representatives', params=query_params).json()
    officials = {}

    for office in response['offices']:
        if office['levels'][0] not in officials.keys():
            officials[office['levels'][0]] = []
        for i in office['officialIndices']:
            off_dict = response['officials'][i]
            official = Official(off_dict['name'], office['name'], off_dict['address'][0])
            if 'emails' in off_dict.keys():
                official.email = off_dict['emails'][0]
            if 'photoUrl' in off_dict.keys():
                official.photo = off_dict['photoUrl']
            officials[office['levels'][0]].append(official)

    officials_list = []
    for level in officials.keys():
        officials_list.append(officials[level])

    return officials_list


"""
Sources for User Profile Model:
1 - https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318
2 - https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/
"""


class UserProfile(models.Model):
    user = models.OneToOneField(auth_models.User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username + " Profile"

    def has_address(self):
        """ Checks if the user has an associated address """
        return self.address == ''

    def government_officials(self):
        """ Returns a list of the government officials presiding over the user's address """
        return government_officials(self.address)
