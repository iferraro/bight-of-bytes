from django.db import models
from django.db.models.fields import BooleanField, CharField
import json

with open('device_data.json', 'r') as myfile:
    device_data=myfile.read()
    
device_obj = json.loads(device_data)

with open('variant_data.json', 'r') as myfile:
    variant_data=myfile.read()
    
variant_obj = json.loads(variant_data)



# Create your models here.

class Variant(models.Model):
    storage = models.IntegerField(),
    price = models.DecimalField(),


class Device(models.Model):
    name = models.CharField(max_length=100),
    base_model = False,
    variants = models.ManyToManyField(Variant)


