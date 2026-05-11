from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    svg_filename = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

   # def get_absolute_url(self):
    #    return reverse('building-list')

class Floor(models.Model):
    TYPES = [('OPEN', 'Open'), ('OFFICE', 'Office')]
    building = models.ForeignKey(Building, related_name='floors', on_delete=models.CASCADE)
    floor_number = models.IntegerField()
    floor_type = models.CharField(max_length=10, choices=TYPES, default='OPEN')
    annual_income = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Floor {self.floor_number} - {self.building.name}"

    def get_absolute_url(self):
        return reverse('building-detail', kwargs={'pk': self.building.id})
