from django.contrib import admin

from .models import *


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    autocomplete_fields = ['locations']
    search_fields = ["name"]

    class Media:
        js = ("js/custom_script.js",)
