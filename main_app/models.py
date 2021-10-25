from django.db import models
#from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, CharField

class Device(models.Model):
    name = models.CharField(max_length=100),
    base_model = False,

class Variant(models.Model):
    storage = models.IntegerField(),
    price = models.DecimalField(),
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

print(type(Variant.device))
