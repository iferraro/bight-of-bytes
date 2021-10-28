from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .forms import VariantForm
from .models import Device, Variant
from .util import populatedb
    
# populatedb()

class DeviceList(ListView):
    model = Device
    fields = ['name']
          
def details(request, dev_pk):
    device = Device.objects.get(id=dev_pk)
    variants = Variant.objects.filter(device_id=dev_pk).order_by('storage')
    print(variants)
    variant_form = VariantForm(request.POST)
    return render(request, 'details.html', {
        'device': device,
        'variants': variants,
        'variant_form': variant_form
        }
    )

class DeviceCreate(CreateView):
    model = Device
    fields = ['name']
    template_name_suffix = '_create_form'
    def form_valid(self, form):
        return super().form_valid(form)

def add_variant(request, dev_pk):
    print(dev_pk)
    var_form = VariantForm(request.POST)
    if var_form.is_valid():
        new_var = var_form.save(commit=False)
        new_var.device_id = dev_pk
        new_var.save()
    return redirect('details', dev_pk=dev_pk)

class VariantUpdate(UpdateView):
    model = Variant
    fields = ['price']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        this_dev_id = Device.objects.get(id=self.object.device_id).id
        return reverse('details', kwargs={'dev_pk': this_dev_id})
    
    



