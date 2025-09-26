# 🔒 Password Lock Security System
## Smart Access Control using Raspberry Pi Pico

![Security System](https://img.shields.io/badge/Security-System-red)
![Raspberry Pi Pico](https://img.shields.io/badge/Raspberry%20Pi-Pico-important)
![Access Control](https://img.shields.io/badge/Access-Control-blue)
![Embedded Systems](https://img.shields.io/badge/Embedded-Systems-success)

---
<br>

- [🔗
My project](https://wokwi.com/projects/439003570471793665)

``` bash
https://wokwi.com/projects/439003570471793665

```
---
## 📖 Introduction

In an era where security is paramount, traditional mechanical locks are increasingly being replaced by intelligent electronic systems. This project implements a **smart password-based lock system** using Raspberry Pi Pico that provides enhanced security, user convenience, and flexible access management.

The system combines multiple components to create a comprehensive security solution:
- **Keypad** for secure password input
- **LCD Display** for user interaction and feedback
- **Servo Motor** as the physical locking mechanism
- **Push Button** for administrative functions

### 🎯 System Capabilities
- ✅ Secure password authentication
- ✅ Visual feedback through LCD
- ✅ Physical lock control via servo
- ✅ Password reset functionality
- ✅ User-friendly interface

---

## 🎯 Project Objectives

| Objective | Status | Details |
|-----------|--------|---------|
| Design password-protected lock system | ✅ Completed | Full implementation |
| Integrate servo motor as actuator | ✅ Completed | Smooth lock/unlock |
| Implement LCD user interface | ✅ Completed | Clear status display |
| Add password management features | ✅ Completed | Secure reset function |

---

## 🔧 Hardware Components

### 📋 Bill of Materials
| Component | Quantity | Purpose | Specifications |
|-----------|----------|---------|---------------|
| Raspberry Pi Pico | 1 | Main Controller | RP2040 Microcontroller |
| 4×4 Matrix Keypad | 1 | Password Input | 16-button interface |
| I2C LCD Display | 1 | User Interface | 16×2 Character |
| Servo Motor | 1 | Lock Mechanism | 180° rotation |
| Push Button | 1 | Admin Control | Tactile switch |
| Breadboard | 1 | Prototyping | 400 points |
| Jumper Wires | 20+ | Connections | Various lengths |

---

## ⚡ Circuit Design & Implementation

### 🔌 System Architecture

```
⌨️ KEYPAD MODULE (4×4 Matrix)
Rows: GP0, GP1, GP2, GP3 (Output)
Cols: GP4, GP5, GP6, GP7 (Input with Pull-down)

📺 LCD MODULE (I2C Interface)
SDA → GP8
SCL → GP9
VCC → 5V
GND → GND

🔓 SERVO MODULE (Lock Actuator)
Signal → GP10 (PWM)
VCC → 5V
GND → GND

🔄 RESET BUTTON
GP11 → Button → GND (Pull-up enabled)
```

### 🎛️ Pin Configuration Table
| Component | Pico GPIO Pins | Function | Notes |
|-----------|---------------|----------|-------|
| Keypad | GP0-GP7 | Password input | 4 rows, 4 columns |
| LCD Display | GP8, GP9 | Status display | I2C communication |
| Servo Motor | GP10 | Lock control | PWM signal |
| Reset Button | GP11 | Admin function | Internal pull-up |

---

## ⚙️ Working Principle

### ⌨️ Keypad Functions
| Key | Function | Description |
|-----|----------|-------------|
| **0-9, A-D** | Password Input | Enter digits/characters |
| **#** | Submit/Confirm | Process password or confirm action |
| ***** | Clear | Reset current input |

---

## 🛠️ Installation & Setup

### 📋 Required Libraries
```python
# Save as requirements.txt
micropython-keypad
micropython-i2c-lcd
micropython-lcd-api
micropython-sevenseg
```

### 🔧 Setup Instructions
1. **Connect components** as per circuit diagram
2. **Install required libraries** on Raspberry Pi Pico
3. **Upload main code** as `main.py`
4. **Power on** the system
5. **Default password**: 1234 (change via reset function)

---

## 🌍 Real-World Applications

### 🏠 Residential Security
- **Smart Door Locks** for homes and apartments
- **Safe and Locker Security** for valuables
- **Garage Access Control** for vehicle security

### 🏢 Commercial Use
- **Office Access Control** for restricted areas
- **Server Room Security** for IT infrastructure
- **Inventory Storage** protection

### 🔧 Industrial Applications
- **Equipment Access Control** for machinery
- **Maintenance Panel Security** for safety
- **Tool Crib Management** for inventory control

---

## ✅ System Specifications

| Parameter | Specification | Details |
|-----------|---------------|---------|
| Password Length | 4+ characters | Configurable minimum |
| Servo Range | 180° | Standard hobby servo |
| Display | 16×2 LCD | I2C interface |
| Keypad | 4×4 Matrix | 16-button input |
| Storage | Internal flash | Password persistence |
| Power | 5V USB | Standard power supply |

---

## 🔒 Security Features

### 🛡️ Protection Mechanisms
- **Password Masking** (***** display)
- **Secure Storage** in internal memory
- **Admin Authentication** for password changes
- **Physical Lock Control** via servo mechanism

### ⚠️ Safety Considerations
- **Default Password** should be changed after setup
- **Secure Location** for physical installation
- **Backup Power** consideration for critical applications

---

## 🔮 Future Enhancements

### 🚀 Advanced Security Features
- **🔐 Multiple User Support** with different access levels
- **📱 Bluetooth/WiFi Connectivity** for remote access
- **📋 Access Logging** with timestamp recording
- **🚨 Intrusion Detection** with buzzer alerts

### 🔧 Technical Improvements
- **🔋 Battery Backup** for power outage protection
- **🌈 OLED Display** for better visibility
- **👆 Touch Keypad** for modern interface
- **🌐 IoT Integration** for smart home systems

---

## 💡 Key Benefits

### 🌟 Security Advantages
- **Enhanced Protection** compared to traditional locks
- **No Physical Keys** to lose or duplicate
- **Quick Password Changes** for access control
- **Audit Trail Capability** for security monitoring

### 💰 Practical Benefits
- **Low Cost** implementation
- **Easy Installation** and setup
- **Minimal Maintenance** required
- **Scalable Design** for various applications

---

## 🎓 Educational Value

This project demonstrates important embedded systems concepts:

### 🏗️ Hardware Integration
- **Microcontroller programming** with Raspberry Pi Pico
- **Sensor/actuator interfacing** (keypad, servo, LCD)
- **Power management** and circuit design
- **Protocol implementation** (I2C, PWM)

### 💻 Software Development
- **State machine design** for system flow
- **User interface programming** for LCD
- **File I/O operations** for password storage
- **Event-driven programming** for keypad input

---


## 🏆 Conclusion & Results

### ✅ Project Success Metrics
- **Fully functional** password authentication system
- **Reliable servo control** for physical locking
- **Intuitive user interface** with LCD feedback
- **Secure password management** with reset capability

### 🌟 Real-World Impact
This project demonstrates how **affordable embedded technology** can create sophisticated security solutions suitable for various residential, commercial, and industrial applications.

---

## 🤝 Contributing

We welcome contributions to enhance this security system:
- **Security improvements** and vulnerability fixes
- **New feature implementations**
- **Documentation enhancements**
- **Testing and validation**

---


*Securing Your World, One Lock at a Time* 💫

