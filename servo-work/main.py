from machine import Pin, PWM, I2C, ADC
import ssd1306
import time

# -------------------------
# Servo Setup
# -------------------------
servo = PWM(Pin(15))
servo.freq(50)   # 50 Hz for servo

# -------------------------
# LED Setup (PWM Brightness)
# -------------------------
led = PWM(Pin(8))
led.freq(1000)   # Higher freq for LED (no flicker)

# -------------------------
# Joystick
# -------------------------
joy_x = ADC(Pin(26))

# -------------------------
# OLED
# -------------------------
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

SCREEN_W = 128
PERIOD_MS = 20
WAVE_Y = 48

# -------------------------
# Functions
# -------------------------
def angle_to_pulse(angle):
    return 1.0 + (angle / 180) * 1.0   # 1–2 ms

def set_servo(pulse_ms):
    duty = (pulse_ms / PERIOD_MS) * 100
    servo.duty_u16(int(duty / 100 * 65535))

def set_led(adc_val):
    led.duty_u16(adc_val)   # Direct brightness control

def draw_pwm(pulse_ms):
    high_w = int((pulse_ms / PERIOD_MS) * SCREEN_W)

    # PWM High
    oled.fill_rect(0, WAVE_Y, high_w, 6, 1)
    # PWM Low
    oled.hline(high_w, WAVE_Y + 6, SCREEN_W - high_w, 1)

# -------------------------
# Main Loop
# -------------------------
while True:
    adc_val = joy_x.read_u16()

    # Servo angle
    angle = int(adc_val * 180 / 65535)
    pulse = angle_to_pulse(angle)
    set_servo(pulse)

    # LED brightness
    set_led(adc_val)
    brightness = int(adc_val * 100 / 65535)

    # OLED Display
    oled.fill(0)
    oled.text("PWM CONTROL DEMO", 0, 0)
    oled.text("Servo:", 0, 12)
    oled.text("Angle: {} deg".format(angle), 0, 22)
    oled.text("LED:", 0, 34)
    oled.text("Bright: {}%".format(brightness), 0, 44)

    draw_pwm(pulse)

    oled.show()
    time.sleep_ms(80)
