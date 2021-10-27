from django.db.models import fields
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import VariantForm
from .models import Device, Variant
from .util import populatedb
    
populatedb()

class DeviceList(ListView):
    model = Device
    fields = ['name']
          
def details(request, pk):
    device = Device.objects.get(id=pk)
    print(device)
    variants = Variant.objects.filter(device_id=pk)
    variant_form = VariantForm(request.POST)
    return render(request, 'details.html', {
        'device': device,
        'variants': variants,
        'variant_form': variant_form
        }
    )

class DeviceCreate(CreateView):
    model = Device
    fields = '__all__'
    
    def form_valid(self, form):
        return super().form_valid(form)




