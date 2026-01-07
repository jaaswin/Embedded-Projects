from machine import Pin, PWM, I2C, ADC
import time
from i2c_lcd import I2cLcd

# LCD setup
I2C_ADDR = 0x27
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Servo
servo = PWM(Pin(15))
servo.freq(50)

# Joystick
joy = ADC(Pin(26))

# Custom characters
HIGH = bytearray([
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111
])

LOW = bytearray([
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
])

lcd.custom_char(0, HIGH)
lcd.custom_char(1, LOW)

def angle_to_pulse(angle):
    return 1.0 + (angle / 180)   # 1–2 ms

def set_servo(pulse):
    duty = (pulse / 20) * 100
    servo.duty_u16(int(duty / 100 * 65535))

while True:
    # Read joystick
    adc = joy.read_u16()
    angle = int(adc * 180 / 65535)
    pulse = angle_to_pulse(angle)

    set_servo(pulse)

    # Convert pulse to LCD blocks
    high_blocks = int((pulse / 20) * 16)
    low_blocks = 16 - high_blocks

    lcd.clear()
    lcd.move_to(0, 0)

    # Draw PWM graph only
    for _ in range(high_blocks):
        lcd.putchar(chr(0))   # HIGH
    for _ in range(low_blocks):
        lcd.putchar(chr(1))   # LOW

    time.sleep(0.15)
