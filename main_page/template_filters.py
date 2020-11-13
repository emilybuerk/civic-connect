"""
Source for template filters
https://stackoverflow.com/questions/8000022/django-template-how-to-look-up-a-dictionary-value-with-a-variable
"""
from django.template.base import Library

register = Library()


@register.filter
def dict_value(dictionary, key):
    return dictionary[key]
