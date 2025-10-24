from machine import Pin
from time import sleep

# Define LED pins
led_pins = [2, 3, 4, 5, 6, 7,8]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Define sensor pins
left_sensor = Pin(14, Pin.IN)
right_sensor = Pin(15, Pin.IN)

while True:
    if left_sensor.value() == 0:
        # Left to Right LED sequence
        for led in leds:
            led.value(1)
            sleep(0.2)
            led.value(0)
    elif right_sensor.value() == 0:
        # Right to Left LED sequence
        for led in reversed(leds):
            led.value(1)
            sleep(0.2)
            led.value(0)
    else:
        # No detection
        for led in leds:
            led.value(0)
