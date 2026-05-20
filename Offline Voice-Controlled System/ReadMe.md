# Offline Voice Control System using VC-02 AI Thinker Module
> Click the button below to jump straight into my projects.
<p align="center">
  <a href="https://youtu.be/4Jcc8QunGvA?si=Zh0MfngLKT0HlIfz" target="_blank">
       <img src="https://img.shields.io/badge/YouTube-%F0%9F%8E%AC-red?style=for-the-badge&logo=youtube" alt="My YouTube channel Badge"/>
  </a>
</p>
<br>
## Project Overview
This project is an **Offline Voice Control System** developed using the VC-02 AI Thinker Voice Recognition Module. The system controls different colored LEDs and a buzzer using predefined voice commands without requiring an internet connection.

The voice commands are integrated and assigned through the official AI Thinker firmware configuration platform:
http://voice.ai-thinker.com/#/

This project demonstrates how offline speech recognition can be used in home automation and embedded systems with low power consumption and fast response time.

---

## Features
- Offline voice recognition
- No internet or cloud dependency
- Control multiple colored LEDs using voice commands
- Voice-controlled buzzer operation
- Fast response and low latency
- Simple embedded system implementation
- Customizable voice commands using AI Thinker firmware tool

---

## Components Used
- VC-02 AI Thinker Voice Recognition Module
- Microcontroller
- Red LED
- Green LED
- Blue LED
- Buzzer
- Resistors
- Breadboard
- Jumper wires
- Power supply

---

## Working Principle
The VC-02 AI Thinker module is trained with predefined voice commands using the AI Thinker firmware configuration platform. After firmware generation and uploading, the module recognizes the stored voice commands offline.

### Working Steps
1. User speaks a predefined voice command.
2. VC-02 module processes the speech offline.
3. The module sends UART/serial data to the controller.
4. The controller checks the received command.
5. Corresponding LED or buzzer is activated.

---

## Voice Commands Used

| Voice Command | Action |
|---|---|
| "Red Light On" | Turns ON Red LED |
| "Red Light Off" | Turns OFF Red LED |
| "Green Light On" | Turns ON Green LED |
| "Green Light Off" | Turns OFF Green LED |
| "Blue Light On" | Turns ON Blue LED |
| "Blue Light Off" | Turns OFF Blue LED |
| "Buzzer On" | Activates buzzer |
| "Buzzer Off" | Deactivates buzzer |

---

## Applications
- Smart home automation
- Offline assistant systems
- Embedded voice control projects
- IoT prototype development
- Assistive technology
- Industrial automation

---

## Advantages
- Completely offline operation
- Enhanced privacy and security
- Low cost implementation
- Easy to configure
- Quick response time
- Low power consumption

---

## Future Enhancements
- Appliance control using relays
- Mobile app integration
- Multi-language voice commands
- IoT cloud connectivity
- Smart scheduling system

---

## Conclusion
This project successfully demonstrates an offline voice-controlled automation system using the VC-02 AI Thinker module. The system efficiently controls LEDs and a buzzer using predefined voice commands without relying on internet connectivity or cloud services.

---

## Setup Instructions

### Firmware Configuration
1. Open the AI Thinker voice platform.
2. Create a new project.
3. Add custom voice commands.
4. Generate firmware.
5. Flash firmware into VC-02 module.

### Hardware Connection
- Connect LEDs to output pins.
- Connect buzzer to control pin.
- Connect VC-02 TX/RX pins using UART communication.
- Power the module properly.

---


