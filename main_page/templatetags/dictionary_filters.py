"""
Sources for template filters
https://stackoverflow.com/questions/8000022/django-template-how-to-look-up-a-dictionary-value-with-a-variable
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#writing-custom-template-filters
"""
from django.template.base import Library

register = Library()


@register.filter
def dict_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return key
