from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Floor(models.Model):
    FLOOR_TYPES = [
        ('RETAIL', 'Retail'),
        ('OFFICE', 'Office'),
    ]
    building = models.ForeignKey(Building, related_name='floors', on_delete=models.CASCADE)
    floor_number = models.IntegerField()
    floor_type = models.CharField(max_length=10, choices=FLOOR_TYPES)
    annual_income = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.building.name} - Floor {self.floor_number}"
