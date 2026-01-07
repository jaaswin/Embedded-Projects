# Servo Motor Control Using Joystick with OLED Display
> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/452380786247314433" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open My Project Badge"/>
  </a>
</p>

<br>

- [🔗
My project](https://wokwi.com/projects/452380786247314433)

``` bash
https://wokwi.com/projects/452380786247314433

```
---

## Introduction

Servo motors are widely used in robotics and automation for precise angular control. Joysticks provide an intuitive way to generate analog control signals. The Raspberry Pi Pico, powered by the RP2040 microcontroller, offers ADC channels, PWM hardware, and I2C communication, making it suitable for such control applications.

This project aims to:

* Read joystick movement using ADC
* Generate a corresponding PWM signal
* Control a servo motor angle
* Display joystick and PWM information on an OLED display

---

## Components Required

* Raspberry Pi Pico (RP2040)
* Servo Motor (SG90 or similar)
* Analog Joystick Module
* OLED Display (SH1106 / SSD1306 – 128×64)
* Connecting Wires
* External 5V supply for servo (recommended)
* Breadboard

---


## Circuit Connections

### Joystick

* VCC → 3.3V (Pico)
* GND → GND
* VRx → GPIO 26 (ADC0)

### Servo Motor

* Signal → GPIO 15 (PWM)
* VCC → 5V (external supply)
* GND → Common GND

### OLED Display (I2C)

* VCC → 3.3V
* GND → GND
* SDA → GPIO 0
* SCL → GPIO 1

---

## Working Principle

When the joystick is moved, the potentiometer inside it changes resistance, producing a varying voltage. The ADC of the Raspberry Pi Pico converts this voltage into a digital value. This value is scaled into a suitable PWM duty cycle. The PWM signal controls the servo motor position. Simultaneously, the OLED displays the joystick reading, PWM duty cycle, and servo angle in real time.

---

## Applications

* Robotic arm control
* Pan-tilt camera systems
* Remote-controlled vehicles
* Educational embedded systems projects



## Conclusion

This project successfully demonstrates servo motor control using a joystick and Raspberry Pi Pico with real-time OLED feedback. It combines analog input processing, PWM generation, and I2C display interfacing, making it an excellent learning platform for embedded systems and robotics enthusiasts.


