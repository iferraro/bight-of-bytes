from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceList.as_view(), name='home'),
    path('devices/<int:pk>/', views.details, name='details'),
    path('new/', views.DeviceCreate.as_view(), name='new')
]