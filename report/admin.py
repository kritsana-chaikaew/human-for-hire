from __future__ import unicode_literals

from django.contrib import admin
from .models import Report

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'init_date')


admin.site.register(Report, AuthorAdmin)