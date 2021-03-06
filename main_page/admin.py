from django.contrib import admin

from .models import Issue, Resource, UserProfile

"""
Source for many-to-many field admin
https://binary-data.github.io/2015/07/21/django-admin-manytomany-inline-enable-add-edit-buttons/
"""


class TopIssueInline(admin.TabularInline):
    model = UserProfile.top_issues.through
    extra = 0


admin.site.register(Issue)
admin.site.register(Resource)


class UserProfileAdmin(admin.ModelAdmin):
    inlines = (TopIssueInline,)
    exclude = ('top_issues',)


admin.site.register(UserProfile, UserProfileAdmin)
