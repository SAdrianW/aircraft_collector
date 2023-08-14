from django.db import models
from django.urls import reverse

# Create your models here.
class Aircraft(models.Model):
    make = models.CharField(max_length=400)
    manufacturer = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    service = models.CharField(max_length=400)
        # Todo: use DateField for both start and end dates, if statement: if still active use auto_now to display 'Currently in Service'
    dimensions = models.CharField(max_length=400)
        # Todo: add template/ validation for format ( ex: 'L: 16.2 m, W: 17.5 m, H: 4.5 m' )
    max_speed = models.IntegerField()
    cruise_speed = models.IntegerField()
    range = models.IntegerField()
    capacity = models.TextField(max_length=2000)
    
    def __str__(self):
        return f"{self.make} - {self.role}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'aircraft_id': self.id})