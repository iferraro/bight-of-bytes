from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceList.as_view(), name='home'),
    path('devices/<int:dev_pk>/', views.details, name='details'),
    path('devices/<int:dev_pk>/add_var/', views.add_variant, name='add_var'),
    path('variants/<int:pk>/update/', views.VariantUpdate.as_view(), name='upd_var'),
    path('new/', views.DeviceCreate.as_view(), name='new')
]