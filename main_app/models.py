from django.db import models
from django.urls import reverse
from datetime import date

MAINTAIN = (
   ('R', 'Repairs'),
   ('F', 'Re-fuel'),
   ('A', 'Re-arm'),
   ('S', 'Re-supply'),
)


# Create your models here.
class Airbase(models.Model):
    airbase_name = models.CharField(max_length=400)
    location = models.CharField(max_length=400)
    country = models.CharField(max_length=400)
    airbase_type = models.CharField(max_length=400)
    area_km2 = models.DecimalField(max_digits=9, decimal_places=3)
    runway_length_km = models.CharField(max_length=400)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.airbase_name

    def get_absolute_url(self):
        return reverse('airbases_detail', kwargs={'pk': self.id})


class Aircraft(models.Model):
    make = models.CharField(max_length=400)
    manufacturer = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    crew = models.CharField(max_length=400)
    service_years = models.CharField(max_length=400)
    ''' Todo?: use DateField for both start and end dates, if statement: if still active use auto_now to display 'Currently in Service'
            Alternativly; leave as char field so entires s like (Jan 12 1954 - 08/22/1998) are possible. 
            Though this does leave less control over data recived, it allows greater freedom of expression.
    '''     
    # dimensions = models.CharField(max_length=400) 
        # dimensions better seperated
        # need to add units to title, would do this in new.html... if I had one
    length_m = models.DecimalField(max_digits=9, decimal_places=3)
    width_m = models.DecimalField(max_digits=9, decimal_places=3)
    height_m = models.DecimalField(max_digits=9, decimal_places=3)
    powerplant = models.CharField(max_length=400)
    max_speed_kmh = models.DecimalField(max_digits=9, decimal_places=3)
    cruise_speed_kmh = models.DecimalField(max_digits=9, decimal_places=3)
    range_km = models.DecimalField(max_digits=9, decimal_places=3)
    max_altitude_m = models.DecimalField(max_digits=9, decimal_places=3)
    capacity = models.TextField(max_length=2000)
    airbases = models.ManyToManyField(Airbase)
    
    def __str__(self):
        return f"{self.make} - {self.role}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'aircraft_id': self.id})
    
    def maintain_today(self):
        return self.maintainance_set.filter(date=date.today()).count() >= len(MAINTAIN)-1 
    
class Maintainance(models.Model):
    date = models.DateField('Maintainace Date')
    maintain = models.CharField(
        max_length=1,
        choices= MAINTAIN,
        default=MAINTAIN[0][0]
        )
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_maintain_display()} on {self.date}'

    class Meta:
        ordering = ['-date']
