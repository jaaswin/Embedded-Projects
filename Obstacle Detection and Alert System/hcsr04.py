#librarie file hcsr04

from machine import Pin, time_pulse_us
from time import sleep_us

class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=30000):
        self.trigger = Pin(trigger_pin, mode=Pin.OUT)
        self.echo = Pin(echo_pin, mode=Pin.IN)
        self.echo_timeout_us = echo_timeout_us

    def distance_cm(self):
        self.trigger.low()
        sleep_us(2)
        self.trigger.high()
        sleep_us(10)
        self.trigger.low()

        try:
            duration = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            distance = (duration * 0.0343) / 2
            return round(distance, 2)
        except OSError:
            return None

