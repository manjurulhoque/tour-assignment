from django.db import models

from locations.models import Location


class Tour(models.Model):
    locations = models.ManyToManyField(Location)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    minimum_duration = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return "Name: {}, {} locations".format(self.name, self.locations.count())
