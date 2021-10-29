from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .forms import VariantForm
from .models import Device, Variant

def signup(request):
    print("made it to signup")
    error_message = ''
    if request.method == 'POST':
        print("POST")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Success!")
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign-up, try again'
    print("Not a post")
    form = UserCreationForm()
    return render(request, 'registration/signup.html',
        {'form': form, 'error_message': error_message}
    )

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

class DeviceCreate(LoginRequiredMixin, CreateView):
    model = Device
    fields = ['name']
    template_name_suffix = '_create_form'
    def form_valid(self, form):
        return super().form_valid(form)

@login_required
def add_variant(request, dev_pk):
    print(dev_pk)
    var_form = VariantForm(request.POST)
    if var_form.is_valid():
        new_var = var_form.save(commit=False)
        new_var.device_id = dev_pk
        new_var.save()
    return redirect('details', dev_pk=dev_pk)

class VariantUpdate(LoginRequiredMixin, UpdateView):
    model = Variant
    fields = ['price']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        this_dev_id = Device.objects.get(id=self.object.device_id).id
        return reverse('details', kwargs={'dev_pk': this_dev_id})
    