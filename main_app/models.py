from django.db import models
from django.urls import reverse
#from django.contrib.auth.models import User

class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'dev_pk': self.pk})

class Variant(models.Model):
    storage = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)