import RPi.GPIO as GPIO
import time
from gpiozero import Button

# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to use
blue_button_pin = 16
green_button_pin = 12
yellow_button_pin = 21
red_button_pin = 20
red_LED_pin = 13
blue_LED_pin = 26
green_LED_pin = 19

green_button = Button(green_button_pin)
yellow_button = Button(yellow_button_pin)

# Set up the GPIO pin as an output
GPIO.setup(red_button_pin, GPIO.OUT)
GPIO.setup(red_LED_pin, GPIO.OUT)    

try:
    
    while(True):

        if yellow_button.is_pressed:
            GPIO.output(green_LED_pin, GPIO.LOW)
            print(f"Pin {red_LED_pin} is turned OFF.")
            break
        if green_button.is_pressed:
            GPIO.output(green_LED_pin, GPIO.HIGH)
            print(f"Pin {green_LED_pin} is turned ON.")
    
finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
