from django.db import models

class Shelf(models.Model):
    label = models.CharField(max_length=80)
