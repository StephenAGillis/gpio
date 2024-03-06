import RPi.GPIO as GPIO
import time

# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to use
blue_button = 16
green_button = 12
yellow_button = 21
red_button = 20
red_LED = 13
blue_LED = 26
green_LED = 19

# Set up the GPIO pin as an output
GPIO.setup(red_button, GPIO.OUT)
GPIO.setup(red_LED, GPIO.OUT)    

try:
    
    while(True):

        if yellow_button.is_pressed:
            GPIO.output(green_LED, GPIO.LOW)
            print(f"Pin {red_LED} is turned OFF.")
            break
        if green_button.is_pressed:
            GPIO.output(green_LED, GPIO.HIGH)
            print(f"Pin {green_LED} is turned ON.")
    
finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
