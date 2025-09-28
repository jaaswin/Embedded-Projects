from machine import Pin, ADC, I2C
import utime
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# -------------------- Pins --------------------
MQ2_AO = ADC(26)

BUZZER = Pin(15, Pin.OUT)
LED = Pin(14, Pin.OUT)       # LED indicator for UNSAFE

# LCD I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=10000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# -------------------- Gas Detection --------------------
ALARM_PPM = 25000 # Unsafe threshold

def read_gas_voltage():
    raw = MQ2_AO.read_u16()
    voltage = (raw / 65535) * 3.3 * 1.5  # scale to ~0-5V
    return voltage

def voltage_to_ppm(voltage):
    ppm = int((voltage / 3.3) * 20000)  # scale 0–3.3V to 0–20000 ppm approx.
    return ppm

# -------------------- Main Loop --------------------
lcd.clear()
lcd.putstr("Gas Monitor ")
utime.sleep(2)

while True:
    gas_voltage = read_gas_voltage()
    ppm = voltage_to_ppm(gas_voltage)

    if ppm > ALARM_PPM:
        status = "Warning : unsafe!"
        BUZZER.value(1)
        LED.value(1)
    else:
        status = "Good air quality"
        BUZZER.value(0)
        LED.value(0)

    # LCD display: line1 = status, line2 = ppm
    lcd.clear()
    lcd.putstr("{}\n{} ppm".format(status, ppm))

    utime.sleep(0.5)
