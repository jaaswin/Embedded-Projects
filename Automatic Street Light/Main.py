from machine import Pin
from time import sleep
sen = Pin(4, Pin.IN)
led = Pin(11, Pin.OUT)
while True:
    senv = sen.value()
    if senv==1:
        led.value(1)
        sleep(0.5)
    else:
        led.value(0)
        sleep(0.5)