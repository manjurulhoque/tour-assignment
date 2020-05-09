from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255, error_messages={'required': 'Location name is required'})
    x_coordinates = models.FloatField(error_messages={'required': 'Enter valid x coordinate'})
    y_coordinates = models.FloatField(error_messages={'required': 'Enter valid y coordinate'})
    description = models.TextField(error_messages={'required': 'Description is required'})
    min_time = models.FloatField(error_messages={'required': 'Minimum time is required'})

    def __str__(self):
        return f"Name: {self.name}, Minimum Time: {self.min_time}"
