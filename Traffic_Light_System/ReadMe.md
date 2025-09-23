## 🚦 Traffic Light System Using Raspberry Pi Pico and 7-Segment Display

A smart traffic management system prototype using Raspberry Pi Pico.

<br>

- [🔗
My project](https://wokwi.com/projects/436559267534476289)

---


## 🚦 Introduction

![Problem](https://img.shields.io/badge/Problem-Traffic%20Congestion-red)
![Solution](https://img.shields.io/badge/Solution-Smart%20Lights-green)

Traffic congestion and accidents are major challenges in urban areas worldwide. This project implements an intelligent traffic light control system using a Raspberry Pi Pico microcontroller to help regulate vehicle movement and enhance road safety.

### Key Features

- ✅ Three-phase traffic light control (Red, Yellow, Green)
- ✅ Real-time countdown display using 7-segment display
- ✅ Configurable timing for each phase
- ✅ Continuous cycle operation simulating real traffic
- ✅ Easy to modify and expand for advanced features

---

## 🎯 Objectives

| Objective                | Status    | Description                               |
|--------------------------|-----------|-------------------------------------------|
| Design traffic light system | ✅ Complete | Raspberry Pi Pico based control system     |
| Countdown display        | ✅ Complete | 7-segment display integration             |
| Real-world simulation    | ✅ Complete | Realistic traffic light sequencing        |
| Educational value        | ✅ Complete | Learning embedded systems concepts        |

---

## 📊 Components Required

### Hardware Components

| Component          | Quantity | Specification         | Purpose           |
|--------------------|----------|----------------------|-------------------|
| Raspberry Pi Pico  | 1        | RP2040 Microcontroller | Main controller  |
| Red LED            | 1        | 5mm, 20mA            | Stop signal       |
| Yellow LED         | 1        | 5mm, 20mA            | Warning signal    |
| Green LED          | 1        | 5mm, 20mA            | Go signal         |
| 220Ω Resistors     | 10       | 1/4W                 | Current limiting  |
| 7-Segment Display  | 1        | Common Cathode       | Countdown display |
| Breadboard         | 1        | 400 points           | Prototyping       |
| Jumper Wires       | 20       | Male-to-Male         | Connections       |
| USB Cable          | 1        | Micro USB            | Power & Programming |

### Software Requirements

- MicroPython firmware for Raspberry Pi Pico
- Thonny IDE or any MicroPython compatible editor

---

## 🔌 Circuit Design

### Pin Configuration Table

| Component         | GPIO Pin | Physical Pin | Description                |
|-------------------|----------|--------------|----------------------------|
| Red LED           | GPIO 0   | Pin 1        | Traffic Stop Signal        |
| Yellow LED        | GPIO 1   | Pin 2        | Traffic Warning Signal     |
| Green LED         | GPIO 2   | Pin 4        | Traffic Go Signal          |
| 7-Segment A       | GPIO 3   | Pin 5        | Segment A control          |
| 7-Segment B       | GPIO 4   | Pin 6        | Segment B control          |
| 7-Segment C       | GPIO 5   | Pin 7        | Segment C control          |
| 7-Segment D       | GPIO 6   | Pin 9        | Segment D control          |
| 7-Segment E       | GPIO 7   | Pin 10       | Segment E control          |
| 7-Segment F       | GPIO 8   | Pin 11       | Segment F control          |
| 7-Segment G       | GPIO 9   | Pin 12       | Segment G control          |
| GND               | GND      | Pin 3,8,13...| Common ground              |

***

#### Operation Flow

1. **System Initialization:** All components are initialized
2. **Red Phase:** Red LED illuminates with 5-second countdown
3. **Transition:** Smooth transition between phases
4. **Green Phase:** Green LED with 5-second countdown
5. **Warning Phase:** Yellow LED with 3-second countdown
6. **Cycle Repeat:** Continuous operation

---

## 💻 Installation & Setup

### Step 1: Hardware Assembly

- Place Raspberry Pi Pico on breadboard
- Connect LEDs with current-limiting resistors
- Wire 7-segment display segments
- Ensure proper ground connections

### Step 2: Software Setup

```bash
# Install MicroPython on Raspberry Pi Pico
1. Download MicroPython firmware from official site
2. Hold BOOTSEL button while connecting USB
3. Drag and drop firmware .uf2 file
4. Pico will reboot with MicroPython
```

### Step 3: Code Upload

- Open Thonny IDE or preferred editor
- Connect to Raspberry Pi Pico
- Copy the code below
- Save as `Main.py` for automatic execution

---

## 🌟 Applications

### Current Implementation

- ✅ **Educational Tool:** Learn embedded systems and traffic management
- ✅ **Prototype Development:** Base for advanced traffic systems
- ✅ **Programming Practice:** MicroPython and hardware interaction

### Future Expansion Possibilities

- 🚀 **IoT Integration:** Remote monitoring and control
- 🚀 **Sensor Addition:** Vehicle detection using IR sensors
- 🚀 **Multiple Lanes:** Four-way intersection control
- 🚀 **Emergency Priority:** Ambulance/fire truck detection
- 🚀 **Adaptive Timing:** Traffic density-based timing adjustment



## ✅ Conclusion

### Project Achievements

- ✅ Successfully designed and implemented traffic light system
- ✅ Integrated 7-segment display for countdown functionality
- ✅ Created realistic traffic light sequencing
- ✅ Demonstrated embedded systems programming concepts

### Educational Value

This project provides hands-on experience with:

- Microcontroller programming using MicroPython
- GPIO pin management and control
- LED and display interfacing
- Real-time system design
- Problem-solving and debugging skills

### Impact and Significance

The traffic light system serves as an excellent foundation for understanding intelligent transportation systems. It demonstrates how simple microcontrollers can solve real-world problems and paves the way for more advanced smart city applications.



⭐ If you find this project helpful, please give it a star! ⭐


_Last updated: sep 2025_  
_Compatible with Raspberry Pi Pico and MicroPython_