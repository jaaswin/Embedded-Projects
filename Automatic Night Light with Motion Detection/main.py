from machine import Pin
from time import sleep
sen = Pin(26, Pin.IN)
led = Pin(5, Pin.OUT)
pir = Pin(15,Pin.OUT)
while True:
    senv = sen.value()
    pirv = pir.value()
    if senv==1:
        if pirv==1: 
            led.value(1)
            print("motion de..")
        print("sen 1")
        sleep(0.5)
    else:
        print("sen 0")
        led.value(0)
        sleep(0.5)
