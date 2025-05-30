from os import name
from django.db import models
from django.forms import FileField, ImageField

categorias = [
    ("mantenimiento", "MANTENIMIENTO"),
    ("reparacion", "REPARACION"),
    ("actividad", "actividad"),
]
estado = [
    ("finalizado", "FINALIZADO"),
    ("pendiente", "PENDIENTE"),
    ("asignado", "ASIGNADO"),
    ("cancelado", "CANCELADO"),
]


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=150, blank=False)
    categories = models.CharField(max_length=15, choices=categorias)
    status = models.CharField(max_length=15, choices=estado)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    detalles = models.TextField(max_length=500, blank=True)
    local = models.CharField(max_length=10, blank=True)
    evidencias = models.FileField(blank=True)
    detalle_final = models.TextField(blank=True)
    asignado = models.CharField(max_length=20, blank=True)
    realizado = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return f"{self.local} - {self.categories} - {self.task_name}"
