from django.contrib import admin

from .models import Issue, Resource, UserProfile

admin.site.register(Issue)
admin.site.register(Resource)
admin.site.register(UserProfile)