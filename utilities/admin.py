from django.contrib import admin

from . import models

from django.conf import settings

# Register your models here.

admin.site.register(models.Electricity)
admin.site.register(models.Water)
admin.site.register(models.Petrol)

if settings.DEBUG:
    admin.site.site_header = "MeadowManager (Debug)"
else:
    admin.site.site_header = "MeadowManager (Prod)"

admin.site.site_title = "DEF"
admin.site.index_title = "Welcome to MeadowManager"