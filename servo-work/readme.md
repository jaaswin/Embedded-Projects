
# Joystick Controlled Servo Motor Angle and LED Brightness with OLED Display using Raspberry Pi Pico

---

## Introduction

Embedded systems combine hardware and software to perform dedicated functions. In this project, a **joystick** is used as a human interface device to control two different outputs using a **Raspberry Pi Pico**:

* The **angle of a servo motor**
* The **brightness of an LED**

Both outputs are controlled using **PWM (Pulse Width Modulation)**, and the real-time values are displayed on an **OLED display**. This project demonstrates how PWM can control different actuators using the same principle but with different behavior.

---

## Objectives

* To read analog values from a joystick using Raspberry Pi Pico ADC
* To control servo motor angle using PWM
* To control LED brightness using PWM
* To display joystick values, servo angle, and LED duty cycle on an OLED display
* To understand and explain the PWM concept through practical implementation

---

## Components Required

* Raspberry Pi Pico (RP2040)
* Joystick Module (X-axis used)
* Servo Motor (SG90 or equivalent)
* LED
* 220Ω Resistor
* OLED Display (128x64, I2C – SSD1306/SH1106)
* Breadboard
* Jumper Wires
* USB Cable

---

## Block Diagram Description

1. Joystick provides analog voltage based on movement
2. Raspberry Pi Pico reads the analog value using ADC
3. PWM signal is generated based on joystick position
4. PWM controls:

   * Servo motor angle
   * LED brightness
5. OLED displays live system information


---

## PWM (Pulse Width Modulation) Concept



### 7.2 PWM in LED Brightness Control

* Human eyes perceive brightness based on average power
* Higher duty cycle → LED ON longer → Brighter LED
* Lower duty cycle → LED ON shorter → Dim LED

Example:

* 25% duty cycle → Dim light
* 50% duty cycle → Medium brightness
* 100% duty cycle → Full brightness

---

### 7.3 PWM in Servo Motor Control

Servo motors interpret PWM differently:

* Frequency is fixed at 50 Hz (20 ms period)
* Pulse width determines angle

Typical Values:

* 0.5 ms pulse → 0°
* 1.5 ms pulse → 90°
* 2.5 ms pulse → 180°

Here, PWM controls **position**, not speed or brightness.

---

### 7.4 Same PWM, Different Behavior

| Device | PWM Role    | Controlled Parameter |
| ------ | ----------- | -------------------- |
| LED    | Duty Cycle  | Brightness           |
| Servo  | Pulse Width | Angle                |

This project clearly shows how the same PWM technique controls different actuators.

---

## Working Principle

1. Joystick is moved left or right
2. Pico reads analog value using ADC
3. Value is mapped to:

   * Servo angle (0°–180°)
   * LED PWM duty cycle (0–65535)
4. PWM signals are updated in real time
5. OLED displays:

   * Joystick ADC value
   * Servo angle
   * LED brightness level

---



## Conclusion

This project successfully demonstrates how PWM can be used to control different devices using a single input device. The joystick provides intuitive control, while the Raspberry Pi Pico efficiently handles ADC, PWM generation, and OLED display. Through this project, the concept of PWM becomes clear by observing its effect on LED brightness and servo motor angle.

---
