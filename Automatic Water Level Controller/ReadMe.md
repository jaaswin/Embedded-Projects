# 🚀 Automatic Water Level Controller

> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/443345805846860801" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open My Project Badge"/>
  </a>
</p>

<br>

- [🔗
My project](https://wokwi.com/projects/443345805846860801)

``` bash
https://wokwi.com/projects/443345805846860801

```
---


## 🎯 Project Overview

This project implements an **Automatic Water Level Controller** using Raspberry Pi Pico that intelligently manages water tanks by monitoring levels and controlling pumps automatically. The system prevents overflow, saves electricity, and reduces human intervention in water management.

---

### ✨ Key Features
- ✅ **Real-time water level monitoring** using ultrasonic sensor
- ✅ **Automatic pump control** with hysteresis
- ✅ **Manual override** capability
- ✅ **Visual status display** on LCD
- ✅ **Motor status indication** with LED
- ✅ **Expandable architecture** for additional features

## 🛠 Components Required

| Component                | Quantity | Purpose                   |
|--------------------------|----------|---------------------------|
| Raspberry Pi Pico        | 1        | Main microcontroller      |
| HC-SR04 Ultrasonic Sensor| 1        | Water level measurement   |
| Relay Module             | 1        | Motor control interface   |
| 16x2 I2C LCD Display     | 1        | Status display            |
| Slide Switch             | 1        | Manual control            |
| LED                      | 1        | Motor status indicator    |
| Buzzer                   | 1        | Alert system              |
| Jumper Wires             | -        | Connections               |
| Breadboard               | 1        | Circuit assembly          |
| Power Supply (5V)        | 1        | Power source              |

## 🔌 Circuit Connections

### 📍 Pin Configuration

| Component                | Raspberry Pi Pico Pin |
|--------------------------|----------------------|
| Ultrasonic Sensor TRIG   | GP3                  |
| Ultrasonic Sensor ECHO   | GP2                  |
| Relay Module             | GP15                 |
| Slide Switch             | GP14                 |
| LCD SDA                  | GP0                  |
| LCD SCL                  | GP1                  |

### 🔧 Block Diagram
```
+----------------------------+
|     Raspberry Pi Pico      |
+----------------------------+
    |        |        |      |
    |        |        |      |
 Ultrasonic  LCD    Relay   Switch
  Sensor           Module     |
    |               |         |
    |               |         |
 Water Tank        LED      Manual
                 (Motor)   Control
```

## ⚙️ Installation & Setup

### Prerequisites
- MicroPython firmware on Raspberry Pi Pico
- Required libraries: `lcd_api.py`, `i2c_lcd.py`
- Thonny IDE or similar MicroPython environment

### Wiring Instructions
1. Connect ultrasonic sensor to GP2 and GP3
2. Wire LCD display using I2C (GP0, GP1)
3. Connect relay to GP15 with LED indicator
4. Install slide switch on GP14 with pull-down resistor
5. Ensure proper power supply to all components

## 🔄 Working Principle

### 🤖 Automatic Mode Operation
1. **Low Water Level** (< 100 cm): Motor turns ON automatically
2. **High Water Level** (> 300 cm): Motor turns OFF automatically  
3. **Intermediate Level**: Maintains current state (hysteresis)

### 👨‍💼 Manual Mode
- Slide switch override forces motor ON regardless of water level
- System returns to automatic mode when switch is turned off

### 📊 Real-time Monitoring
- Continuous distance measurement
- Live status display on LCD
- Visual feedback through LED


## 🏗 Hardware Assembly Guide

### Step-by-Step Construction
1. **Mount Components**: Secure all components on breadboard
2. **Power Connections**: Connect 5V and GND rails properly
3. **Sensor Placement**: Position ultrasonic sensor above tank
4. **Motor Connection**: Connect relay to pump motor circuit
5. **Testing**: Verify all connections before powering

### 🔍 Safety Considerations
- Use proper insulation for high-voltage connections
- Ensure waterproofing for sensor and connections
- Include fuse protection for motor circuit

## 📊 Applications

### 🏠 Residential Use
- Automatic overhead tank management
- Prevention of water overflow
- Electricity conservation

### 🏭 Industrial Applications
- Chemical tank level monitoring
- Liquid storage management
- Process automation

### 🌾 Agricultural Implementations
- Smart irrigation systems
- Reservoir management
- Drip irrigation control

## 🚀 Future Enhancements

### 🔮 Planned Features
- **IoT Integration**: Remote monitoring via Wi-Fi/ESP8266
- **Mobile App**: Real-time notifications and control
- **Multiple Tanks**: Support for complex water systems
- **Data Logging**: Historical water usage patterns
- **Weather Integration**: Smart watering based on forecast

### 🔧 Technical Upgrades
- **Real Motor Implementation**: Replace LED with actual pump
- **Advanced Alerts**: Buzzer patterns for different conditions
- **Power Backup**: Battery support for power outages
- **Web Dashboard**: Remote monitoring interface



## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest new features.

**⭐ If this project helped you, please give it a star on GitHub!**



