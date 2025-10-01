# mpu6050.py

from machine import I2C
import time

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        # Wake up MPU6050 (it starts in sleep mode)
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')
        time.sleep(0.1)

    def read_raw_data(self, reg):
        high = self.i2c.readfrom_mem(self.addr, reg, 1)[0]
        low = self.i2c.readfrom_mem(self.addr, reg + 1, 1)[0]
        value = (high << 8) | low
        if value > 32768:
            value -= 65536
        return value

    def get_accel(self):
        x = self.read_raw_data(0x3B)
        y = self.read_raw_data(0x3D)
        z = self.read_raw_data(0x3F)
        return {'x': x, 'y': y, 'z': z}

    def get_gyro(self):
        x = self.read_raw_data(0x43)
        y = self.read_raw_data(0x45)
        z = self.read_raw_data(0x47)
        return {'x': x, 'y': y, 'z': z}

    def get_temp(self):
        temp_raw = self.read_raw_data(0x41)
        temp_c = temp_raw / 340.0 + 36.53
        return temp_c
