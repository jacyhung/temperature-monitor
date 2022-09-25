from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
import os
import subprocess
import board
from adafruit_bme280 import basic as adafruit_bme280
from apscheduler.schedulers.background import BackgroundScheduler

# Create your views here.
def index(request):
    return render(request,'index.html')

def scheduleTask():
    scheduler = BackgroundScheduler()
    scheduler.add_job(querySensor, 'interval', seconds=1)
    scheduler.start()

def querySensor():
    print("Querying sensor data... updating database values")
    i2c = board.I2C()
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    sensor = Sensordata.objects.get(pk=1)

    sensor.temperature = round((bme280.temperature * (9 / 5) + 32), 1)
    sensor.humidity = round(bme280.humidity, 1)
    sensor.pressure = round(bme280.pressure, 1)
    temperature = sensor.temperature
    sensor.save()

def temp(request):
    sensor = Sensordata.objects.get(pk=1)
    temperature = sensor.temperature
    return HttpResponse(temperature)

def humidity(request):
    sensor = Sensordata.objects.get(pk=1)
    humidity = sensor.humidity
    return HttpResponse(humidity)

def pressure(request):
    sensor = Sensordata.objects.get(pk=1)
    pressure = sensor.pressure
    return HttpResponse(pressure)

def altitude(request):
    i2c = board.I2C()
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    sensor = Sensordata.objects.get(pk=1)
    sensor.humidity = round(bme280.altitude, 1)
    altitude = sensor.altitude
    sensor.save()
    return HttpResponse(altitude)

def cputemp(request):
    cpuTempOutput = subprocess.check_output('vcgencmd measure_temp', shell=True)
    string = str(cpuTempOutput)
    cpuTempValue = string[7:11]

    sensor = Sensordata.objects.get(pk=1)
    sensor.cputemp = cpuTempValue
    sensor.save()
    return HttpResponse(sensor.cputemp)