from django.db import models
#from django.contrib.auth.models import User

class Device(models.Model):
    name = models.CharField(max_length=100)
    base_model = models.BooleanField()

class Variant(models.Model):
    storage = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

print(type(Variant.device))
