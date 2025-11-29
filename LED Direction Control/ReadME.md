# LDR Sensor–Based LED Direction Control (Raspberry Pi Pico)
> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/445709043753958401" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open My Project Badge"/>
  </a>
</p>

<br>

- [🔗
My project](https://wokwi.com/projects/445709043753958401)

``` bash
https://wokwi.com/projects/445709043753958401

```
An intelligent light-direction indicator using two LDR (Light Dependent Resistor) sensors and a Raspberry Pi Pico. Six LEDs arranged in a line light sequentially to indicate the direction of the stronger light source: left-to-right when the left sensor is brighter, and right-to-left when the right sensor is brighter. Implemented in MicroPython.
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



