from django.forms import ModelForm, fields
from .models import Device, Variant

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

class VariantForm(ModelForm):
    class Meta:
        model = Variant
        exclude = ['device']