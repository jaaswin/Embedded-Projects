# 🚨 Obstacle Detection and Alert System
## Smart Safety Solution using Raspberry Pi Pico & Ultrasonic Sensor

![Embedded Systems](https://img.shields.io/badge/Embedded-Systems-green)
![Raspberry Pi Pico](https://img.shields.io/badge/Raspberry%20Pi-Pico-red)
![Safety System](https://img.shields.io/badge/Safety-System-orange)
![Real-time Monitoring](https://img.shields.io/badge/Real--time-Monitoring-blue)

---
<br>

- [🔗
My project](https://wokwi.com/projects/437461592162958337)

``` bash
https://wokwi.com/projects/437461592162958337

```


## 📖 Introduction

Obstacle detection is a critical technology in modern automation, robotics, and safety systems. Traditional proximity warning systems often lack multi-sensory feedback, reducing their effectiveness in real-world scenarios.

This project implements an **intelligent obstacle detection system** using Raspberry Pi Pico that provides comprehensive alerts through visual, audible, and display interfaces. The system ensures timely warnings to prevent accidents and enhance safety in various applications.

### 🎯 System Overview
- **Ultrasonic Distance Measurement** - Accurate object detection
- **Multi-Alert System** - LED, buzzer, and LCD notifications
- **Real-time Monitoring** - Continuous distance tracking
- **User-friendly Interface** - Clear status display

---

## 🎯 Project Objectives

| Objective | Status | Achievement |
|-----------|--------|-------------|
| ✅ Design obstacle detection system | Completed | Fully functional |
| ✅ Implement multi-alert feedback | Completed | LED + Buzzer + LCD |
| ✅ Real-time distance display | Completed | LCD integration |
| ✅ Practical safety application | Successful | Ready for deployment |

---

## 🔧 Hardware Components

### 📋 Bill of Materials
| Component | Quantity | Purpose | Specification |
|-----------|----------|---------|---------------|
| Raspberry Pi Pico | 1 | Main Controller | RP2040 Microcontroller |
| HC-SR04 Ultrasonic Sensor | 1 | Distance Measurement | 2cm-400cm range |
| I2C LCD Display | 1 | Status Display | 16×2 Character |
| LED (Red) | 1 | Visual Alert | 5mm Indicator |
| Buzzer | 1 | Audible Alert | Active Buzzer |
| 220Ω Resistor | 1 | LED Protection | Current Limiting |
| Breadboard | 1 | Prototyping | 400 points |
| Jumper Wires | 15+ | Connections | Male-to-Male |

---

## ⚡ Circuit Design & Implementation

### 🔌 System Architecture Diagram

```
📡 SENSOR MODULE (HC-SR04)
VCC → 5V
GND → Ground
TRIG → GP3
ECHO → GP2

📺 DISPLAY MODULE (I2C LCD)
SDA → GP0
SCL → GP1
VCC → 5V
GND → Ground

💡 ALERT MODULE
LED: GP14 → 220Ω → LED(+) → LED(-) → GND
BUZZER: GP15 → Buzzer(+) → Buzzer(-) → GND
```

### 🎛️ Pin Configuration Table
| Component | Raspberry Pi Pico Pin | Function |
|-----------|---------------------|----------|
| Ultrasonic Sensor | GP3 (TRIG), GP2 (ECHO) | Distance Sensing |
| I2C LCD Display | GP0 (SDA), GP1 (SCL) | Status Display |
| LED Indicator | GP14 | Visual Alert |
| Buzzer | GP15 | Audible Alert |
| Power | 5V/3.3V, GND | System Power |

---

## ⚙️ Working Principle

### 📊 Alert Threshold System
| Distance Range | Alert Level | LED | Buzzer | LCD Message |
|----------------|-------------|-----|--------|-------------|
| **> 100 cm** | Safe | OFF | OFF | "No Object Nearby" |
| **≤ 100 cm** | Warning | ON | ON | "Object Detected" |
| **Sensor Error** | Error | OFF | OFF | "Sensor Error" |

---


## 🛠️ Installation & Setup

### 📋 Required Libraries
```python
# Save as requirements.txt
micropython-hcsr04
micropython-i2c-lcd
```

### 🔧 Setup Instructions
1. **Connect hardware** as per circuit diagram
2. **Upload libraries** to Raspberry Pi Pico
3. **Copy main code** to `main.py`
4. **Power on** the system
5. **Monitor output** via serial console

---

## 🌍 Real-World Applications

### 🚗 Automotive Safety
- **Parking Assistance Systems**
- **Blind Spot Detection**
- **Collision Avoidance**

### ♿ Assistive Technology
- **Smart Blind Sticks** for visually impaired
- **Obstacle Avoidance** for mobility aids
- **Navigation Assistance** systems

### 🏭 Industrial Automation
- **Robot Collision Prevention**
- **Conveyor Belt Safety**
- **Warehouse Automation**

### 🏠 Smart Home
- **Automatic Door Opening**
- **Security Perimeter Monitoring**
- **Smart Furniture Safety**

---

## ✅ System Specifications

| Parameter | Specification | Details |
|-----------|---------------|---------|
| Detection Range | 2cm - 400cm | HC-SR04 Capability |
| Alert Threshold | 100cm | Configurable |
| Response Time | < 100ms | Real-time operation |
| Display | 16×2 LCD | I2C interface |
| Power Supply | 5V DC | USB or external |
| Operating Current | < 200mA | Energy efficient |


---

## 💡 Key Features & Benefits

### 🌟 Multi-Sensory Alerts
- **Visual** - LED indicator for quick glance
- **Audible** - Buzzer for attention-grabbing alerts
- **Display** - LCD for detailed information

### 🛡️ Safety Advantages
- **Early Warning System** - Prevents accidents
- **Reliable Detection** - Ultrasonic technology
- **User-friendly** - Clear status indications

### 💰 Economic Benefits
- **Low Cost** - Affordable components
- **Easy Maintenance** - Simple design
- **Scalable** - Adaptable for various applications

---

## 🎓 Educational Value

This project demonstrates essential embedded systems concepts:

### 🏗️ Hardware Integration
- Sensor interfacing (Ultrasonic HC-SR04)
- Display systems (I2C LCD)
- Alert mechanisms (LED + Buzzer)
- Power management

### 💻 Software Development
- Real-time programming
- Sensor data processing
- Multi-threading concepts
- Error handling

### 🔬 Scientific Principles
- Speed of sound calculations
- Wave propagation physics
- Distance measurement techniques
- System calibration
---

## 🏆 Conclusion & Results

### ✅ Project Success Metrics
- **Fully functional prototype** with reliable operation
- **Accurate distance measurement** within specifications
- **Effective multi-alert system** for comprehensive warnings
- **User-friendly interface** with clear status display

### 🌟 Impact Potential
This system demonstrates how **affordable embedded technology** can create practical safety solutions with real-world applications in automotive, industrial, and assistive domains.

---

