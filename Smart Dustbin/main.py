from machine import Pin, PWM
import time

# Pins
TRIG = Pin(5, Pin.OUT)
ECHO = Pin(18, Pin.IN)
servo = PWM(Pin(13), freq=50)

# Servo helper
def servo_write(angle):
    # Convert angle (0-180) to duty (40-115)
    duty = int((angle / 180) * 75) + 40
    servo.duty(duty)

# Get distance using HC-SR04
def get_distance():
    TRIG.off()
    time.sleep_us(2)
    TRIG.on()
    time.sleep_us(10)
    TRIG.off()

    while ECHO.value() == 0:
        pass
    start = time.ticks_us()

    while ECHO.value() == 1:
        pass
    end = time.ticks_us()

    duration = end - start
    distance = (duration * 0.034) / 2
    return distance

# Initialize servo
servo_write(0)

print("Smart Dustbin Ready...")

while True:
    dist = get_distance()
    print("Distance:", dist, "cm")

    if dist > 0 and dist < 20:
        servo_write(90)       # Open lid
        time.sleep(3)
        print("open")
        servo_write(0)        # Close lid

    time.sleep(0.2)
