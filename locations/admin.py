from django.contrib import admin

from .models import *


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    search_fields = ["name"]
    save_as = True
