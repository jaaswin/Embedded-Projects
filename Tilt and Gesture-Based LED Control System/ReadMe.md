# Tilt and Gesture-Based LED Control System using MPU6050 and Raspberry Pi Pico

## Project Overview
This embedded systems project demonstrates a real-time tilt and gesture recognition system using the MPU6050 6-axis IMU (Inertial Measurement Unit) sensor with a Raspberry Pi Pico microcontroller. The system interprets orientation data to control LEDs, providing visual feedback for different gesture inputs. This implementation showcases practical motion sensing applications in modern embedded systems.


---
> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/437457996173988865" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open My Project Badge"/>
  </a>
</p>

---
## Introduction

Motion sensing and gesture recognition have become fundamental technologies in modern electronics, from smartphone interfaces to advanced robotics. This project creates an intuitive control system that translates physical movements into digital commands using the MPU6050 accelerometer and gyroscope sensor paired with a Raspberry Pi Pico.

The system detects tilting motions and directional gestures along three axes (X, Y, Z) and provides immediate visual feedback through corresponding LEDs. This demonstrates core concepts in embedded systems, including sensor interfacing, I²C communication, real-time data processing, and GPIO control.

## Components Required

| Component | Quantity | Specification |
|-----------|----------|---------------|
| Raspberry Pi Pico | 1 | RP2040 Microcontroller |
| MPU6050 Sensor | 1 | 6-axis Accelerometer and Gyroscope |
| LEDs | 3 | Any color (Red, Green, Blue recommended) |
| Resistors | 3 | 220Ω (1/4 Watt) |
| Breadboard | 1 | Standard prototyping board |
| Jumper Wires | Multiple | Male-to-Male and Male-to-Female |
| USB Cable | 1 | Micro-USB for programming and power |

## Hardware Setup

### Circuit Schematic

```
MPU6050 Sensor Connections:
┌─────────────┬─────────────────┐
│ MPU6050     │ RaspberryPiPico │
├─────────────┼─────────────────┤
│ VCC         │ 3.3V (Pin 36)   │
│ GND         │ GND (Pin 38)    │
│ SCL         │ GP1 (Pin 2)     │
│ SDA         │ GP0 (Pin 1)     │
└─────────────┴─────────────────┘

LED Connections:
┌────────────┬──────────────────┬─────────────┐
│ LED        │ Raspberry Pi Pico │ Resistor   │
├────────────┼──────────────────┼─────────────┤
│ LED1 (X)   │ GP15 (Pin 20)    │ 220Ω to GND │
│ LED2 (Y)   │ GP19 (Pin 25)    │ 220Ω to GND │
│ LED3 (Z)   │ GP27 (Pin 32)    │ 220Ω to GND │
└────────────┴──────────────────┴─────────────┘
```

### Physical Connection Guide

1. **Power Connections**:
   - Connect MPU6050 VCC to 3.3V on Pico
   - Connect MPU6050 GND to any GND pin on Pico

2. **I²C Communication**:
   - Connect MPU6050 SDA to GP0 (Pin 1)
   - Connect MPU6050 SCL to GP1 (Pin 2)

3. **LED Outputs**:
   - Connect each LED anode (long leg) to respective GPIO pins
   - Connect each LED cathode (short leg) to 220Ω resistor
   - Connect other end of resistors to GND


## Working Principle

### MPU6050 Sensor Operation
The MPU6050 contains a 3-axis accelerometer and 3-axis gyroscope that measure:
- **Acceleration**: Rate of change of velocity along X, Y, Z axes
- **Angular velocity**: Rotational speed around X, Y, Z axes

For this project, we utilize the accelerometer data to detect tilt and orientation based on gravitational forces.

### Axis Orientation
- **X-axis**: Left-right tilt (Roll)
- **Y-axis**: Forward-backward tilt (Pitch) 
- **Z-axis**: Up-down orientation

### Control Logic

| Axis | Condition | LED State | Gesture |
|------|-----------|-----------|---------|
| X | > +10000 | LED1 ON | Tilt Right |
| X | < -10000 | LED1 OFF | Tilt Left |
| Y | > +10000 | LED2 ON | Forward Tilt |
| Y | < -10000 | LED2 OFF | Backward Tilt |
| Z | > +10000 | LED3 ON | Facing Up |
| Z | < -10000 | LED3 OFF | Facing Down |

The threshold values (±10000) are calibrated based on the sensor's sensitivity and can be adjusted for different applications.

## Software Implementation

### Required Libraries
The project requires the `mpu6050.py` library for interfacing with the sensor. This should be saved to your Raspberry Pi Pico before running the main code.

## Results and Demonstration

### System Performance
The system successfully demonstrates:
- Real-time tilt detection along all three axes
- Immediate LED response to orientation changes
- Stable sensor readings through I²C communication
- Clear visual feedback for each gesture

### Expected Output
When running the system, the serial monitor displays:

```
MPU6050 sensor initialized successfully
Tilt and Gesture LED Control System Started
===========================================
X:    -235 | Y:    15412 | Z:    12456 | X: Neutral | Forward Tilt → LED2 ON | Facing Up → LED3 ON
X:   12568 | Y:      -235 | Z:     1245 | Right Tilt → LED1 ON | Y: Neutral | Z: Neutral
X:  -13579 | Y:    -14256 | Z:   -11568 | Left Tilt → LED1 OFF | Backward Tilt → LED2 OFF | Facing Down → LED3 OFF
```

### Calibration Tips
1. **Threshold Adjustment**: Modify the ±10000 values for different sensitivity
2. **Sensor Placement**: Ensure stable mounting for consistent readings
3. **Environmental Factors**: Avoid vibrations and sudden movements during testing

## Applications

### 1. Human-Computer Interaction
- Gesture-controlled interfaces
- Hands-free device control
- Accessibility tools for impaired users

### 2. Robotics and Automation
- Robot orientation feedback
- Autonomous navigation systems
- Robotic arm position control

### 3. Smart Home Systems
- Gesture-controlled lighting
- Motion-activated appliances
- Security system triggers

### 4. Gaming and Entertainment
- Motion-based game controllers
- Virtual reality interfaces
- Interactive art installations

### 5. Industrial Applications
- Equipment orientation monitoring
- Safety tilt alarms
- Vehicle attitude indicators

## Future Enhancements

### 1. Advanced Gesture Recognition
```python
# Example: Complex gesture detection
def detect_gesture(accel_data, gyro_data):
    # Implement shake, rotate, or pattern recognition
    pass
```

### 2. Wireless Connectivity
- Add Bluetooth/WiFi for remote monitoring
- IoT integration for smart home systems
- Mobile app dashboard

### 3. Additional Outputs
- Servo motor control based on orientation
- LCD display for real-time data
- Buzzer for audio feedback

### 4. Data Logging
- SD card storage for motion data
- Time-stamped orientation history
- Analysis and pattern recognition

### 5. Power Optimization
- Sleep modes for battery operation
- Motion-activated wake-up
- Low-power design techniques

## Conclusion

This Tilt and Gesture-Based LED Control System successfully demonstrates the integration of motion sensing technology with microcontroller-based embedded systems. The project highlights:

- **Practical Implementation**: Real-world application of sensor data processing
- **Educational Value**: Clear demonstration of I²C communication and GPIO control
- **Expandability**: Foundation for more complex motion-based systems
- **Cost-Effectiveness**: Uses affordable, widely available components

The system provides an excellent platform for learning embedded systems development, with potential applications spanning from educational tools to professional automation systems. The modular design allows for easy expansion and customization based on specific requirements.

---



*Feel free to contribute to this project by submitting issues or pull requests!*
