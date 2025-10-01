# main.py

from machine import Pin, I2C
from time import sleep
from mpu6050 import MPU6050

# I2C setup (GP0 = SDA, GP1 = SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# Initialize MPU6050
mpu = MPU6050(i2c)

# Initialize output device (LED on GP15)
led1 = Pin(15, Pin.OUT)
led2=Pin(19,Pin.OUT)
led3=Pin(27,Pin.OUT)
while True:
    accel = mpu.get_accel()
    x = accel['x']
    y = accel['y']
    z = accel['z']
    
    print("Accel X:", x, "Y:", y, "Z:", z)

    # Gesture control logic
    if x > 10000:
        led1.on()
        print("Tilt Right → LED ON")
    elif x < -10000:
        led1.off()
        print("Tilt Left → LED OFF")
    if y > 10000:
        led2.on()
        print("Tilt Right → LED ON")
    elif y < -10000:
        led2.off()
        print("Tilt Left → LED OFF")   
    if z > 10000:
        led3.on()
        print("Tilt Right → LED ON")
    elif z < -10000:
        led3.off()
        print("Tilt Left → LED OFF") 
    sleep(0.5)
