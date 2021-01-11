from django.contrib import admin

from . import models

# Register your models here.
class RainAdmin(admin.ModelAdmin):
    list_display = ('day', 'amount', 'hail',)

admin.site.register(models.Rain, RainAdmin)