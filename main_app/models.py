from django.db import models
from django.db.models.fields import BooleanField, CharField
import json

device_dict = json.loads('device_data.json');
variant_dict = json.loads('variant_data.json');

# Create your models here.

class Variant(models.Model):
    storage = models.IntegerField(),
    price = models.DecimalField(),


class Device(models.Model):
    name = models.CharField(max_length=100),
    base_model = False,
    variants = models.ManyToManyField(Variant)


