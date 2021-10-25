from django.shortcuts import render, redirect
from django.views.generic import ListView
import json

with open('device_data.json', 'r') as myfile:
    device_data = myfile.read()

device_obj = json.loads(device_data)

def home(request):
    devices = device_obj['Devices']
    return render(request, 'home.html', {'preloaded_devices': devices})    



