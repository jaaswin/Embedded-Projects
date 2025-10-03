# Automatic Night Light Using Raspberry Pi Pico

## 1. Project Overview

This project implements an intelligent night light system that automatically illuminates when motion is detected in dark environments. The system combines light sensing and motion detection to create an energy-efficient lighting solution.

![System Block Diagram](https://via.placeholder.com/600x200?text=LDR+%2B+PIR+%E2%86%92+Raspberry+Pi+Pico+%E2%86%92+LED)

## 2. Objective

The purpose of this project is to design a simple embedded system that automatically turns on an LED when motion is detected in a dark environment. This project demonstrates the integration of LDR (light sensor) and PIR motion sensor with a Raspberry Pi Pico, providing hands-on experience with sensor interfacing and conditional logic programming.

## 3. Components Required

| Component | Quantity | Purpose | Specification |
|-----------|----------|---------|---------------|
| Raspberry Pi Pico | 1 | Microcontroller | RP2040 microcontroller |
| PIR Motion Sensor | 1 | Motion detection | HC-SR501 typically |
| LDR (Photoresistor) | 1 | Ambient light sensing | Light-dependent resistor |
| LED | 1 | Night light output | Standard 5mm LED |
| Resistor (220Ω) | 1 | Current limiting for LED | 1/4 Watt |
| Resistor (10kΩ) | 1 | Pull-down for LDR | 1/4 Watt |
| Breadboard | 1 | Prototyping circuit | - |
| Jumper Wires | As needed | Connections | Male-to-male |

## 4. Working Principle

The system operates on a simple but effective logic:

1. **Light Detection**: The LDR continuously monitors ambient light levels
2. **Motion Detection**: The PIR sensor detects movement in its field of view
3. **Decision Logic**: The Raspberry Pi Pico processes both sensor inputs
4. **LED Control**: The LED turns ON only when both conditions are met:
   - Dark environment (LDR detects low light)
   - Motion is present (PIR sensor triggered)

```
[LDR Sensor]  --->|
                 |--> [Raspberry Pi Pico] --> [LED ON/OFF]
[PIR Sensor] --->|
```

## 5. Circuit Connections

### Schematic Diagram

```
+---------------+       +-----------------+
|   LDR         |       | Raspberry Pi    |
|               |       | Pico            |
|   One leg ----|------|-> GP26 (Pin 31)  |
|               |       |                 |
| Other leg ----|--[10kΩ]---> GND         |
+---------------+       |                 |
                        |                 |
+---------------+       |                 |
| PIR Sensor    |       |                 |
|               |       |                 |
| VCC ----------|------|-> 5V            |
| GND ----------|------|-> GND           |
| OUT ----------|------|-> GP15 (Pin 20) |
+---------------+       |                 |
                        |                 |
+---------------+       |                 |
| LED           |       |                 |
|               |       |                 |
| Long leg (+) -|--[220Ω]---> GP5 (Pin 7)|
| Short leg (-)-|------|-> GND           |
+---------------+       +-----------------+
```

### Connection Details

**LDR (Light Dependent Resistor)**
- One leg → GP26 (Pin 31) on Pico
- Other leg → GND via 10kΩ resistor (voltage divider configuration)

**PIR Motion Sensor**
- VCC → 5V (VBUS)
- GND → GND
- OUT → GP15 (Pin 20)

**LED**
- Anode (long leg) → GP5 (Pin 7) through 220Ω resistor
- Cathode (short leg) → GND

### Code Explanation

**Initialization:**
- Sets up GPIO pins for LDR, PIR, and LED
- Configures pins as inputs or outputs appropriately

**Main Loop:**
1. Reads current sensor values from LDR and PIR
2. Implements the decision logic:
   - LED turns ON only when it's dark AND motion is detected
   - Includes a timeout feature to keep LED on for a period after last motion
3. Provides detailed status output for debugging
4. Includes a small delay to prevent excessive processing

**Features:**
- **Debouncing**: Prevents rapid on/off switching
- **Timeout**: Keeps light on for a set time after motion
- **Status Reporting**: Detailed console output for monitoring
- **Energy Efficient**: Only activates when needed

## 7. Calibration and Adjustments

### LDR Calibration
- The LDR circuit acts as a voltage divider
- Adjust the 10kΩ resistor value based on your LDR's characteristics
- Test in different lighting conditions to find optimal thresholds

### PIR Sensor Settings
Most PIR sensors have two potentiometers:
- **Sensitivity**: Adjust detection range (typically 3-7 meters)
- **Time Delay**: How long the output stays high after detection

### LED Timing
Modify the `led_on_time` variable to change how long the LED stays on after motion is no longer detected.

## 8. Applications 

### Practical Applications
- Home security lighting
- Bathroom night lights
- Closet or wardrobe lighting
- Pathway illumination
- Energy-efficient corridor lighting


## 9. Advantages

- **Energy Efficient**: Only consumes power when needed
- **Cost Effective**: Uses inexpensive, readily available components
- **Easy to Build**: Suitable for beginners in embedded systems
- **Customizable**: Easily adjustable sensitivity and timing
- **Educational**: Demonstrates multiple embedded concepts:
  - Sensor interfacing (both analog and digital)
  - Conditional logic implementation
  - GPIO programming
  - Real-time system design


## 11. Conclusion

This project successfully demonstrates the implementation of an automatic night light system using Raspberry Pi Pico. The system effectively combines light sensing (LDR) and motion detection (PIR) to create an intelligent lighting solution that conserves energy while providing illumination when needed.

Through this project, learners gain practical experience with:
- Raspberry Pi Pico GPIO programming
- Sensor integration and interfacing
- Conditional logic implementation
- Embedded system design principles
- Circuit prototyping and debugging

The project serves as an excellent foundation for more advanced home automation and IoT projects, providing a solid understanding of how to make embedded systems responsive to environmental conditions.

---


*Feel free to contribute to this project by submitting issues or pull requests on GitHub!*        