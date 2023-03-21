# autoLikes
Auto-like Tiktok livestreams with a Raspberry Pi 4, rotary encoder, and a servo.


## Rotary Encoder Servo Controller

This program is designed to control a servo motor using a rotary encoder and a push button. It is written in Python and meant to run on a Raspberry Pi. The program reads the rotary encoder's input, updates the servo motor's position accordingly, and resets the position when the push button is pressed.

## Hardware Setup

- Rotary Encoder:
  - Connect RoAPin (Pin A) to Raspberry Pi pin 11
  - Connect RoBPin (Pin B) to Raspberry Pi pin 12
  
- Push Button:
  - Connect BtnPin to Raspberry Pi pin 13

- Servo Motor:
  - Connect ServoPin (signal) to Raspberry Pi pin 7

## Dependencies

To run this program, you will need the RPi.GPIO library. You can install it using pip:

```
pip install RPi.GPIO
```

## Running the Program

To run the program, navigate to the directory containing the script and run:

```
python3 testing.py
