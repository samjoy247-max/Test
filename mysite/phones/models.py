from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
