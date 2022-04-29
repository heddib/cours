from django.contrib import admin
from django.db import models

# Create your models here.
class Cours(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

admin.site.register(Cours)