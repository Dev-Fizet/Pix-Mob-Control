import serial
import time
from pixmob_conversion_funcs import to_arduino_string
from effect_definitions import base_color_effects, tail_codes, special_effects

import tkinter as tk
from tkinter import ttk

# This file lets you send a single command to bracelets over IR by way of an Arduino connected to this computer
# running one of the PixMob_Transmitter sketches in the arduino_sender folder. Note that it may take two or more tries
# to make bracelets react after they have been inactive for a while.

# Set the ALL_CAPS parameters below and run the script.

# Which effect/color to display on the lights. See base_color_effects or special_effects in effect_definitions.py for
# options.
# MAIN_EFFECT = "MAGENTA"
# TAIL_CODE = "FADE_2"

# Optional, set to None if not using. Can use this to modify simple color effects by making them fade in and/or out
# and/or making them display probabilistically. See tail_codes in effect_definitions.py for options.
# WARNING: NOT ALL TAIL CODES ARE COMPATIBLE WITH ALL BRACELETS AND COLORS. It may take some trial and error.
##TAIL_CODE = "FADE_2"

# Which serial port the Arduino is connected to. You can find this with the Arduino IDE or follow these instructions:
# https://www.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html
ARDUINO_SERIAL_PORT = "COM8"

# Baud rate of the serial connection set up on the Arduino. It is 115200 in the included sketches.
ARDUINO_BAUD_RATE = 115200

# Set to True if using a lower power microcontroller (like an Arduino Nano instead of ESP board) and you have issues
WAIT_BEFORE_SEND = False

#################################
arduino = serial.Serial(port=ARDUINO_SERIAL_PORT,baudrate=ARDUINO_BAUD_RATE, timeout=.1)


def Send_Blue():
    print('Blue')
    for i in range(1):
        MAIN_EFFECT = "BLUE"
        TAIL_CODE = "FADE_2"
        if WAIT_BEFORE_SEND:
            time.sleep(2.5)
        if MAIN_EFFECT in base_color_effects:
            effect_bits = base_color_effects[MAIN_EFFECT]
            if TAIL_CODE:
                if TAIL_CODE in tail_codes:
                    effect_bits = effect_bits + tail_codes[TAIL_CODE]
                else:
                    raise Exception(
                        "Invalid tail code name. See tail_codes in effect_definitions.py for options.")
        elif MAIN_EFFECT in special_effects:
            effect_bits = special_effects[MAIN_EFFECT]
            if TAIL_CODE:
                raise Exception("Tail code effects only supported on simple color effects found in base_color_effects of "
                                "effect_definitions.py. Set TAIL_CODE to None or choose a MAIN_EFFECT from base_color_effects "
                                "(instead of special_effects).")
        else:
            raise Exception("Invalid MAIN_EFFECT. See base_color_effects and special_effects in effect_definitions.py for "
                            "options.")

        arduino_string_ver = to_arduino_string(effect_bits)

        arduino.write(bytes(arduino_string_ver, 'utf-8'))
        time.sleep(0.1)
        print("Command sent to Arduino.")

def Send_Green():
    print('Green')
    for i in range(1):
        MAIN_EFFECT = "GREEN"
        TAIL_CODE = "FADE_2"
        if WAIT_BEFORE_SEND:
            time.sleep(2.5)
        if MAIN_EFFECT in base_color_effects:
            effect_bits = base_color_effects[MAIN_EFFECT]
            if TAIL_CODE:
                if TAIL_CODE in tail_codes:
                    effect_bits = effect_bits + tail_codes[TAIL_CODE]
                else:
                    raise Exception(
                        "Invalid tail code name. See tail_codes in effect_definitions.py for options.")
        elif MAIN_EFFECT in special_effects:
            effect_bits = special_effects[MAIN_EFFECT]
            if TAIL_CODE:
                raise Exception("Tail code effects only supported on simple color effects found in base_color_effects of "
                                "effect_definitions.py. Set TAIL_CODE to None or choose a MAIN_EFFECT from base_color_effects "
                                "(instead of special_effects).")
        else:
            raise Exception("Invalid MAIN_EFFECT. See base_color_effects and special_effects in effect_definitions.py for "
                            "options.")

        arduino_string_ver = to_arduino_string(effect_bits)

        arduino.write(bytes(arduino_string_ver, 'utf-8'))
        time.sleep(0.1)
        print("Command sent to Arduino.")

def Send_Red():
    print('Red')
    for i in range(1):
        MAIN_EFFECT = "RED"
        TAIL_CODE = "FADE_2"
        if WAIT_BEFORE_SEND:
            time.sleep(2.5)
        if MAIN_EFFECT in base_color_effects:
            effect_bits = base_color_effects[MAIN_EFFECT]
            if TAIL_CODE:
                if TAIL_CODE in tail_codes:
                    effect_bits = effect_bits + tail_codes[TAIL_CODE]
                else:
                    raise Exception(
                        "Invalid tail code name. See tail_codes in effect_definitions.py for options.")
        elif MAIN_EFFECT in special_effects:
            effect_bits = special_effects[MAIN_EFFECT]
            if TAIL_CODE:
                raise Exception("Tail code effects only supported on simple color effects found in base_color_effects of "
                                "effect_definitions.py. Set TAIL_CODE to None or choose a MAIN_EFFECT from base_color_effects "
                                "(instead of special_effects).")
        else:
            raise Exception("Invalid MAIN_EFFECT. See base_color_effects and special_effects in effect_definitions.py for "
                            "options.")

        arduino_string_ver = to_arduino_string(effect_bits)

        arduino.write(bytes(arduino_string_ver, 'utf-8'))
        time.sleep(0.1)
        print("Command sent to Arduino.")


def Send_Blue_Fast():
    print('Blue')
    for i in range(1):
        MAIN_EFFECT = "BLUE"
        TAIL_CODE = ""
        if WAIT_BEFORE_SEND:
            time.sleep(2.5)
        if MAIN_EFFECT in base_color_effects:
            effect_bits = base_color_effects[MAIN_EFFECT]
            if TAIL_CODE:
                if TAIL_CODE in tail_codes:
                    effect_bits = effect_bits + tail_codes[TAIL_CODE]
                else:
                    raise Exception(
                        "Invalid tail code name. See tail_codes in effect_definitions.py for options.")
        elif MAIN_EFFECT in special_effects:
            effect_bits = special_effects[MAIN_EFFECT]
            if TAIL_CODE:
                raise Exception("Tail code effects only supported on simple color effects found in base_color_effects of "
                                "effect_definitions.py. Set TAIL_CODE to None or choose a MAIN_EFFECT from base_color_effects "
                                "(instead of special_effects).")
        else:
            raise Exception("Invalid MAIN_EFFECT. See base_color_effects and special_effects in effect_definitions.py for "
                            "options.")

        arduino_string_ver = to_arduino_string(effect_bits)

        arduino.write(bytes(arduino_string_ver, 'utf-8'))
        time.sleep(0.1)
        print("Command sent to Arduino.")

def Send_Green_Fast():
    print('Green')
    for i in range(1):
        MAIN_EFFECT = "GREEN"
        TAIL_CODE = ""
        if WAIT_BEFORE_SEND:
            time.sleep(2.5)
        if MAIN_EFFECT in base_color_effects:
            effect_bits = base_color_effects[MAIN_EFFECT]
            if TAIL_CODE:
                if TAIL_CODE in tail_codes:
                    effect_bits = effect_bits + tail_codes[TAIL_CODE]
                else:
                    raise Exception(
                        "Invalid tail code name. See tail_codes in effect_definitions.py for options.")
        elif MAIN_EFFECT in special_effects:
            effect_bits = special_effects[MAIN_EFFECT]
            if TAIL_CODE:
                raise Exception("Tail code effects only supported on simple color effects found in base_color_effects of "
                                "effect_definitions.py. Set TAIL_CODE to None or choose a MAIN_EFFECT from base_color_effects "
                                "(instead of special_effects).")
        else:
            raise Exception("Invalid MAIN_EFFECT. See base_color_effects and special_effects in effect_definitions.py for "
                            "options.")

        arduino_string_ver = to_arduino_string(effect_bits)

        arduino.write(bytes(arduino_string_ver, 'utf-8'))
        time.sleep(0.1)
        print("Command sent to Arduino.")

def Send_Red_Fast():
    print('Red')
    for i in range(1):
        MAIN_EFFECT = "RED"
        TAIL_CODE = ""
        if WAIT_BEFORE_SEND:
            time.sleep(2.5)
        if MAIN_EFFECT in base_color_effects:
            effect_bits = base_color_effects[MAIN_EFFECT]
            if TAIL_CODE:
                if TAIL_CODE in tail_codes:
                    effect_bits = effect_bits + tail_codes[TAIL_CODE]
                else:
                    raise Exception(
                        "Invalid tail code name. See tail_codes in effect_definitions.py for options.")
        elif MAIN_EFFECT in special_effects:
            effect_bits = special_effects[MAIN_EFFECT]
            if TAIL_CODE:
                raise Exception("Tail code effects only supported on simple color effects found in base_color_effects of "
                                "effect_definitions.py. Set TAIL_CODE to None or choose a MAIN_EFFECT from base_color_effects "
                                "(instead of special_effects).")
        else:
            raise Exception("Invalid MAIN_EFFECT. See base_color_effects and special_effects in effect_definitions.py for "
                            "options.")

        arduino_string_ver = to_arduino_string(effect_bits)

        arduino.write(bytes(arduino_string_ver, 'utf-8'))
        time.sleep(0.1)
        print("Command sent to Arduino.")
        
root = tk.Tk()
root.config(width=300, height=200)
root.title("Test PixMob Fizet Lab")
boton = ttk.Button(text="BLUE", command=Send_Blue)
boton.place(x=50, y=50)
boton = ttk.Button(text="GREEN", command=Send_Green)
boton.place(x=50, y=75)
boton = ttk.Button(text="RED", command=Send_Red)
boton.place(x=50, y=(100))
boton = ttk.Button(text="BLUE FAST", command=Send_Blue_Fast)
boton.place(x=120, y=50)
boton = ttk.Button(text="GREEN FAST", command=Send_Green_Fast)
boton.place(x=120, y=75)
boton = ttk.Button(text="RED FAST", command=Send_Red_Fast)
boton.place(x=120, y=100)
root.mainloop()
