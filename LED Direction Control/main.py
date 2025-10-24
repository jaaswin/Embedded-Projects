from machine import Pin, ADC
from time import sleep

# Define LED pins
led_pins = [2, 3, 4, 5, 6, 7]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Define LDR sensor pins (ADC)
left_ldr = ADC(26)   # GP26
right_ldr = ADC(27)  # GP27

# Threshold difference to detect direction
threshold = 1000

while True:
    left_value = left_ldr.read_u16()
    right_value = right_ldr.read_u16()

    if left_value - right_value > threshold:
        # Light detected on left → flow left to right
        for led in leds:
            led.value(1)
            sleep(0.2)
            led.value(0)

    elif right_value - left_value > threshold:
        # Light detected on right → flow right to left
        for led in reversed(leds):
            led.value(1)
            sleep(0.2)
            led.value(0)

    else:
        # No significant light difference
        for led in leds:
            led.value(0)

    sleep(0.1)
