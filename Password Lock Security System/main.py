from machine import Pin, I2C, PWM
from time import sleep
from keypad import Keypad
from i2c_lcd import I2cLcd
import os

# ---------------- LCD Setup ----------------
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
lcd_addr = i2c.scan()[0]
lcd = I2cLcd(i2c, lcd_addr, 2, 16)

# ---------------- Servo Setup ----------------
servo = PWM(Pin(10))
servo.freq(50)

def servo_lock():
    servo.duty_u16(2000)  # lock position

def servo_unlock():
    servo.duty_u16(7000)  # unlock position

servo_lock()

# ---------------- Keypad Setup ----------------
rows = [Pin(x, Pin.OUT) for x in (0,1,2,3)]
cols = [Pin(x, Pin.IN, Pin.PULL_DOWN) for x in (4,5,6,7)]
keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]
keypad = Keypad(rows, cols, keys)

# ---------------- Password File ----------------
PASS_FILE = "password.txt"

def read_password():
    if PASS_FILE in os.listdir():
        with open(PASS_FILE) as f:
            return f.read().strip()
    else:
        with open(PASS_FILE, "w") as f:
            f.write("1234")
        return "1234"

def save_password(new_pass):
    with open(PASS_FILE, "w") as f:
        f.write(new_pass)

password = read_password()

# ---------------- Push Button ----------------
reset_btn = Pin(11, Pin.IN, Pin.PULL_UP)

# ---------------- Main Logic ----------------
entered = ""

def show_entered():
    lcd.clear()
    lcd.putstr("Enter Password:")
    lcd.move_to(0,1)
    lcd.putstr("*" * len(entered))

while True:
    if reset_btn.value() == 0:
        # Reset password mode
        lcd.clear()
        lcd.putstr("Old Password:")
        temp = ""
        while True:
            k = keypad.get_key()
            if k:
                if k == '#':
                    if temp == password:
                        lcd.clear()
                        lcd.putstr("New Password:")
                        newp = ""
                        while True:
                            nk = keypad.get_key()
                            if nk:
                                if nk == '#':
                                    save_password(newp)
                                    password = newp
                                    lcd.clear()
                                    lcd.putstr("Updated!")
                                    sleep(1)
                                    break
                                elif nk == '*':
                                    newp = ""
                                    lcd.move_to(0,1)
                                    lcd.putstr(" " * 16)
                                else:
                                    newp += nk
                                    lcd.move_to(0,1)
                                    lcd.putstr("*" * len(newp))
                            sleep(0.1)
                        break
                    else:
                        lcd.clear()
                        lcd.putstr("Wrong Password")
                        sleep(1)
                        break
                elif k == '*':
                    temp = ""
                    lcd.move_to(0,1)
                    lcd.putstr(" " * 16)
                else:
                    temp += k
                    lcd.move_to(0,1)
                    lcd.putstr("*" * len(temp))
            sleep(0.1)

    k = keypad.get_key()
    if k:
        if k == '#':
            if entered == password:
                lcd.clear()
                lcd.putstr("Access Granted")
                servo_unlock()
                sleep(3)
                servo_lock()
            else:
                lcd.clear()
                lcd.putstr("Access Denied")
            entered = ""
            sleep(1)
        elif k == '*':
            entered = ""
        else:
            entered += k
        show_entered()

    sleep(0.1)
