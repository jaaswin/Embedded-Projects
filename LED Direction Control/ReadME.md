# LDR Sensor–Based LED Direction Control (Raspberry Pi Pico)

An intelligent light-direction indicator using two LDR (Light Dependent Resistor) sensors and a Raspberry Pi Pico. Six LEDs arranged in a line light sequentially to indicate the direction of the stronger light source: left-to-right when the left sensor is brighter, and right-to-left when the right sensor is brighter. Implemented in MicroPython.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Hardware Required](#hardware-required)  
- [Circuit / Wiring](#circuit--wiring)  
- [Software](#software)  
  - [Installation](#installation)  
  - [Usage](#usage)  
  - [Calibration](#calibration)  
- [How It Works](#how-it-works)  
- [Configuration Options](#configuration-options)  
- [Troubleshooting](#troubleshooting)  
- [Possible Enhancements](#possible-enhancements)  
- [Repository Structure](#repository-structure)  
- [Contributing](#contributing)  
- [License & Credits](#license--credits)

---

## Project Overview

This project demonstrates analog sensor interfacing, threshold-based decision logic, and sequential LED control using a Raspberry Pi Pico running MicroPython. The Pico reads two LDRs via ADC inputs, compares light intensity, and animates a 6-LED array to indicate the direction of the dominant light source.

---

## Features

- Real-time light intensity comparison between left and right LDRs  
- Directional LED animation: left-to-right and right-to-left  
- Debounce logic to avoid rapid flicker when direction toggles  
- Simple calibration routine to determine a practical threshold  
- Small, low-power, educational hardware/software example

---

## Hardware Required

- Raspberry Pi Pico (RP2040) — 1  
- LDR (Photoresistor) — 2 (e.g., GL5528)  
- Fixed resistors for LDR voltage dividers — 2 × 10 kΩ  
- LEDs (5 mm) — 6  
- Current-limiting resistors for LEDs — 6 × 220 Ω  
- Breadboard and jumper wires  
- 3.3V power source (Pico's 3.3V from USB)  
- Micro USB cable (for programming/power)

---

## Circuit / Wiring

Summary (text diagram):

- LDR voltage dividers:
  - +3.3V → 10 kΩ → ADC (GP26 for left, GP27 for right) → LDR → GND  
  - The ADC pin should read the node between the fixed resistor and the LDR.
- LEDs:
  - GP2 → 220 Ω → LED1 → GND  
  - GP3 → 220 Ω → LED2 → GND  
  - GP4 → 220 Ω → LED3 → GND  
  - GP5 → 220 Ω → LED4 → GND  
  - GP6 → 220 Ω → LED5 → GND  
  - GP7 → 220 Ω → LED6 → GND

Notes:
- Ensure common ground between the Pico and any other components.
- The ADCs on Pico return values in 0–65535 when using read_u16() in MicroPython (12-bit ADC scaled to 16-bit).

For a detailed wiring diagram, see Documentation/Circuit_Diagram.fzz (Fritzing).

---

## Software

This project uses MicroPython running on the Raspberry Pi Pico.

Included scripts:
- `Source_Code/main.py` — main application (sensor read, decision, LED animation)  
- `Source_Code/calibration.py` — simple interactive calibration helper

### Installation

1. Flash MicroPython UF2 to the Pico:
   - Download the latest MicroPython firmware for the Raspberry Pi Pico from micropython.org.
   - Follow Pico instructions to flash the UF2 file.

2. Copy files to the Pico:
   - Use Thonny, ampy, rshell, or the Pico's mass storage mode to copy `main.py` (and optionally `calibration.py`) to the device.

3. Power the Pico (via USB). Open the serial REPL (e.g., Thonny) to view prints and debug output.

### Usage

- After copying `main.py` to the Pico, it will run automatically on boot.
- The program continuously samples both LDRs and:
  - If |left - right| > THRESHOLD, it triggers a directional animation.
  - If the difference is less than or equal to THRESHOLD, all LEDs stay off.
- Use `calibration.py` to determine a good THRESHOLD for your environment.

Example snippet from `main.py` (already included in the repository):

```python
# (Example usage)
# Place main.py on the Pico and power it. Open serial monitor to see debug prints.
```

### Calibration

Run `calibration.py` (from the Pico REPL or via Thonny) and follow prompts:

1. Cover the RIGHT LDR and press Enter — script captures one reading.
2. Cover the LEFT LDR and press Enter — script captures the other reading.
3. Script outputs a recommended threshold (e.g., 30% of a measured max). Adjust `THRESHOLD` constant in `main.py` accordingly.

---

## How It Works (high level)

1. Read averaged ADC values from the two LDR channels.
2. Compute the absolute difference.
3. If difference exceeds the configured threshold:
   - If left > right: animate LEDs from GP2 → GP7 (left-to-right).
   - If right > left: animate LEDs from GP7 → GP2 (right-to-left).
4. If difference is below threshold: switch LEDs off.
5. A debounce timeout prevents immediate flips between directions.

---

## Configuration Options

Edit constants in `main.py`:

- THRESHOLD — minimum absolute ADC difference to consider direction meaningful  
- ANIMATION_DELAY — time each LED stays on during the sequence (seconds)  
- SAMPLE_DELAY — delay between sensor sampling cycles (seconds)  
- DEBOUNCE_TIME — minimum ms between direction-change animations (milliseconds)

Calibration is recommended after deploying in the intended environment.

---

## Troubleshooting

- LEDs don’t light:
  - Check LED orientation (long lead = anode), resistor wiring, and Pico GPIO pin mapping.
- Sensors read constant / strange values:
  - Verify voltage divider wiring. Confirm ADC pins are GP26/GP27.
- Flickering / rapid switching:
  - Increase THRESHOLD or DEBOUNCE_TIME. Consider adding averaging or filtering.
- No output on serial:
  - Confirm Pico is powered and connected. Use Thonny to open the REPL.

---

## Possible Enhancements

- Adaptive thresholding (automatic re-calibration in changing ambient light).
- Hysteresis to reduce toggling around the threshold.
- Use more sensors (4 or 8 LDRs) for better angular resolution.
- Replace discrete LEDs with an addressable RGB strip (NeoPixel) for richer animations.
- Add servo motors for physical light tracking (solar tracker / light-seeking robot).
- Display live sensor values on an OLED screen or via a web dashboard (with an ESP module).

---

## Repository Structure

LDR-LED-Direction-Control/
- Documentation/
  - README.md
  - Circuit_Diagram.fzz
  - Technical_Specifications.pdf
- Source_Code/
  - main.py
  - calibration.py
  - requirements.txt
- Hardware/
  - BOM.csv
  - Schematics/
  - PCB_Design/
- Media/
  - Demo_Videos/
  - Images/
  - Working_Prototype/
- Additional_Resources/
  - Datasheets/
  - Tutorials/
  - References/

---

## Contributing

Contributions are welcome:
- Open issues for bugs or feature requests
- Submit pull requests with improvements or new features
- Share your projects and enhancements

Please follow standard GitHub workflow and include clear descriptions and tests where appropriate.

---

## License & Credits

- Author: [Your Name]  
- Adapted/Documented by: Project Contributors  
- License: MIT (or choose your preferred license)

Replace the author name and license as appropriate for your repository.

---

Enjoy experimenting with the LDR directional LED controller!  
Happy hacking — point some light and watch the LEDs follow.
