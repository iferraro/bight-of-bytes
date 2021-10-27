from django.db.models import fields
from django.forms import ModelForm
from .models import Device, Variant
from main_app import models

class VariantForm(ModelForm):
    class Meta:
        model = Variant
        exclude = ['device']
    # def __init__(self, *args, **kwargs):
    #     print(kwargs)
    #     # self.fields['device'] = kwargs['pk']
