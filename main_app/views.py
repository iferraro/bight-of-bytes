from django.db import connection
from django.db.models import fields
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import VariantForm
from .models import Device, Variant
import json

from main_app import models

def populatedb():
    with open('device_data.json', 'r') as myfile:
        device_data = myfile.read()

    device_obj = json.loads(device_data)

    with connection.cursor() as cursor:
        try:
            devices = device_obj['Devices']

            for i in range(len(devices)):
               device = devices[i] 
               param_list = [ device["id"], device["name"], device["base_model"] ]
               cursor.execute("INSERT INTO main_app_device (id, name, base_model) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", param_list)
               ## HERE WE CANT VALIDATE THE VARIANTS BC NO VARIANT ID IN JSON

            cursor.execute("SELECT count(*) FROM main_app_variant")
            returnCount = cursor.fetchone()
            count = returnCount[0]
            for device in devices:
                print(device['name'])
            print(count, "<---- ok, no variants")
            if(count == 0):
                for i in range(len(devices)):
                   device = devices[i] 
                   variants = device["variants"]
                   for j in range(len(variants)):
                       variant = variants[j]
                       param_list = [ device["id"], variant["price"], variant["storage"] ]
                       cursor.execute("INSERT INTO main_app_variant (device_id, price, storage) VALUES (%s, %s, %s)", param_list)
        finally: 
            cursor.close()
    
class DeviceList(ListView):
    model = Device
    fields = ['name']
          
def details(request, pk):
    device = Device.objects.get(id=pk)
    print(device)
    # variants = Variant.objects.get(device_id=pk)
    variant_form = VariantForm(request.POST)
    return render(request, 'details.html', {
        'device': device,
        # 'variants': variants,
        'variant_form': variant_form
        }
    )

class DeviceCreate(CreateView):
    model = Device
    fields = '__all__'
    def form_valid(self, form):
        return super().form_valid(form)




