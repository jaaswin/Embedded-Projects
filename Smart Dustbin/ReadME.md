# Smart Dustbin Using ESP32
> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/450055741350402049" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open My Project Badge"/>
  </a>
</p>

<br>

- [🔗
My project](https://wokwi.com/projects/450055741350402049)

``` bash
https://wokwi.com/projects/450055741350402049

```

##  Overview

This project implements a **Smart Dustbin** using an ESP32 running **MicroPython**. The system detects the presence of a hand or object using an ultrasonic sensor (HC-SR04) and automatically opens the lid via a PWM-controlled servo motor. After a short delay, the lid closes again.

The project is simple, low-cost, and ideal for learning:

* GPIO control
* PWM for servo
* Distance measurement
* Real-time embedded programming
* MicroPython scripting

---

##  Features

* Fully touchless lid operation
* Accurate distance measurement
* Fast response powered by ESP32
* Safe servo handling using external 5V supply
* Easily customizable threshold & timings
* Low power consumption

---

##  Hardware Components

* ESP32 Development Board
* Ultrasonic Sensor (HC-SR04)
* Servo Motor (SG90/MG90S)
* External 5V power supply for servo
* Jumper wires
* Dustbin with movable lid
* Common ground connection

---

##  Circuit Connections

### Ultrasonic Sensor (HC-SR04)

| HC-SR04 Pin | ESP32 Pin |
| ----------- | --------- |
| VCC         | 5V        |
| GND         | GND       |
| TRIG        | GPIO 5    |
| ECHO        | GPIO 18   |

### Servo Motor

| Servo Pin | ESP32 Pin   |
| --------- | ----------- |
| VCC       | External 5V |
| GND       | Common GND  |
| Signal    | GPIO 13     |

**Note:**
The servo must not be powered from the ESP32's 5V pin. Use an external 5V source and connect the grounds together.

---

##  Working Principle

1. The ultrasonic sensor emits pulses and measures the time for returning echoes.
2. ESP32 calculates the distance using that duration.
3. If an object is detected within a set range (<20 cm), the servo rotates to open the dustbin lid.
4. After a fixed delay, the lid returns to its closed position.
5. The system continuously monitors for new objects.

This ensures a clean, hygienic, fully automatic waste-disposal process.

---

##  Applications

* Smart home automation
* Public sanitation systems
* Dustbins in hospitals, malls, schools
* IoT-powered smart cities
* Contactless product design research

---

##  Conclusion

This Smart Dustbin project demonstrates how embedded systems and MicroPython can be combined to build real-world automation solutions. It is simple, scalable, and an excellent foundation for more advanced IoT applications.

