#main.py for obstacle detection with ultrasonic sensor

from hcsr04 import HCSR04
from machine import Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd

# Init I2C and LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd_addr = i2c.scan()[0]
lcd = I2cLcd(i2c, lcd_addr, 2, 16)

# Init ultrasonic sensor, LED, buzzer
sensor = HCSR04(trigger_pin=3, echo_pin=2)
led = Pin(14, Pin.OUT)
buzzer = Pin(15, Pin.OUT)

lcd.clear()
lcd.putstr("Ultrasonic Sensor\nInitializing...")
sleep(2)
lcd.clear()

while True:
    distance = sensor.distance_cm()
    lcd.clear()
    
    if distance:
        lcd.putstr("Distance: {:.1f} cm".format(distance))
        print("Distance:", distance, "cm")

        if distance <= 100:
            led.on()
            print("led on")
            buzzer.on()
            print("buzzer ring")
            lcd.move_to(0, 1)
            lcd.putstr("Object Detected")
            sleep(1)
        else:
            led.off()
            buzzer.off()
            lcd.move_to(0, 1)
            lcd.putstr("No Object Nearby")
    else:
        lcd.putstr("Sensor Error")
        led.off()
        buzzer.off()

    sleep(0.5)


