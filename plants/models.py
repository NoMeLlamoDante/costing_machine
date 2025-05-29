from pyexpat import model
from django.db import models


# Create your models here.
class Plant(models.Model):
    # Comercial info
    comercial_name = models.CharField(max_length=30)
    sucursal_number = models.PositiveSmallIntegerField(unique=True, default=1)
    ubicacion = models.URLField(blank=True)
    start_date = models.DateField(blank=True)
    # payments
    # Owner
    # Purifier
    purifier_info = models.TextField(blank=True, max_length=250)

    # Auto-vending
    no_ventanas = models.PositiveSmallIntegerField(default=1)
    precio_fria = models.FloatField(max_length=5, default=7)
    precio_tiempo = models.FloatField(max_length=5, default=14)