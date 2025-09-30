from machine import Pin, I2C
import utime
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# --- Pins ---
TRIG = Pin(3, Pin.OUT)
ECHO = Pin(2, Pin.IN)
RELAY = Pin(15, Pin.OUT)          # Relay input pin
SLIDE_SWITCH = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Manual control

# --- LCD setup (I2C 16x2) ---
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
LCD_ADDR = 0x27  # Change if your LCD uses 0x3F
lcd = I2cLcd(i2c, LCD_ADDR, 2, 16)

# --- Motor initial state ---
RELAY.value(0)  # LED OFF
motor_state = 0

# --- Distance thresholds ---
ON_DISTANCE = 100   # cm, LED ON if water level < 100 cm
OFF_DISTANCE = 300  # cm, LED OFF if water level > 300 cm

def get_distance():
    """Measure distance using ultrasonic sensor"""
    TRIG.low()
    utime.sleep_us(2)
    TRIG.high()
    utime.sleep_us(10)
    TRIG.low()
    
    while ECHO.value() == 0:
        start = utime.ticks_us()
    while ECHO.value() == 1:
        end = utime.ticks_us()
        
    duration = end - start
    distance = (duration * 0.0343) / 2  # cm
    return distance

while True:
    distance = get_distance()
    manual = SLIDE_SWITCH.value()  # 1=Manual ON, 0=Auto

    # --- Control Motor/LED ---
    if manual == 1:
        motor_state = 1   # Manual: LED ON
    else:
        # Auto mode
        if distance < ON_DISTANCE:
            motor_state = 1  # LED ON
        elif distance > OFF_DISTANCE:
            motor_state = 0  # LED OFF
        # else: keep previous state (hysteresis)

    RELAY.value(motor_state)

    # --- Display on LCD ---
    lcd.clear()
    lcd.putstr("Water: {:.1f}cm\n".format(distance))
    lcd.putstr("Motor: {}".format("ON" if motor_state else "OFF"))

    utime.sleep(1)
