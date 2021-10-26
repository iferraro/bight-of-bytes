from django.urls import path
from . import views

urlpatterns = [
    # path('', views.DeviceList.as_view(), name='home'),
    path('', views.home, name='home'),
    path('<int:pk>/', views.DeviceDetail.as_view(), name='details'),
    path('new/', views.DeviceCreate.as_view(), name='new')
]