from django.db import models
#from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, CharField
import json

with open('device_data.json', 'r') as myfile:
    device_data = myfile.read()

device_obj = json.loads(device_data)

preloaded_devices = device_obj['Devices']
for device in preloaded_devices:
    print(device['name'])

class Device(models.Model):
    name = models.CharField(max_length=100),
    base_model = False,

class Variant(models.Model):
    storage = models.IntegerField(),
    price = models.DecimalField(),
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

print(type(Variant.device))
