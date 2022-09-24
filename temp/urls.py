from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('temp', views.temp, name="temp"),
    path('humidity', views.humidity, name="humidity"),
    path('pressure', views.pressure, name="pressure"),
    path('altitude', views.altitude, name="altitude"),
    path('cputemp', views.cputemp, name="cputemp"),
]
