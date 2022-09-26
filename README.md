# Temperature Monitor
Django web app that grabs temperature &amp; other sensor data from a BME280 sensor with a Raspberry Pi.

![temp](https://user-images.githubusercontent.com/13006956/192176239-e013a4ea-ad9b-40d4-acc9-d9efc6e872f4.gif)


## Features
<ul>
<li>Grabs sensor data via i2c</li>
<li>Web app with live-updating values</li>
<li>Adjustable scheduled interval for querying sensor</li>

</ul>

## Hardware Required
You can technically run this on anything that can run Python and accepts i2c. My arrangement is as follows,

<ul>
<li>Raspberry Pi 4</li>
<li>BME280 Sensor</li>
</ul>

If you wish to run a different temperature sensor, it's important that you install the appropriate libraries for your sensor, and modify the views to grab those sensor values.

!! I've tested the DHT22 sensor, and while it works, the Adafruit Python library I used for it did not allow for it to be queried as often as the BME280. This resulted in multiple errors when querying for multiple 
sensor data at once or too quickly. The BME280 has worked flawlessly and my 1s interval works flawlessly. YMMV. !!

## How to setup

1. `pip3 install -r requirements.txt`
2. `python3 manage.py migrate`
3. `python3 manage.py makemigrations`
4. `python3 manage.py createsuperuser`
<i>(This step is not necessary, although you need to create a Serverdata object either through the Admin GUI or manually. You will get a model does not exist error if you do not create one.)</i>
5. Create your Django secret key
6. `python3 manage.py runserver`

## Credits
<ul>
<li>Adafruit's BME280 Python Library: https://github.com/adafruit/Adafruit_CircuitPython_BME280</li>
<li>Template: https://codepen.io/supah/pen/NNNEqM</li>
</ul>
