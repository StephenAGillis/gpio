import RPi.GPIO as GPIO
import time


# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to use
blue_button= 16
green_button = 12
yellow_button = 21
red_button = 20

red_LED = 13
blue_LED = 26
green_LED = 19

interupt = 23

# Set up the GPIO pin as an output
GPIO.setup(green_button, GPIO.OUT)
GPIO.setup(green_LED, GPIO.OUT)

GPIO.setup(yellow_button, GPIO.OUT)

def led_color(x):
    GPIO.output(x, GPIO.HIGH)
    print(f"Pin {x} is turned ON.")
    
    time.sleep(1)
    
    GPIO.output(x, GPIO.LOW)
    print(f"Pin {x} is turned OFF.")

def setup():
    GPIO.output(interupt, GPIO.HIGH)
    GPIO.output(green_button, GPIO.HIGH)
    GPIO.output(blue_button, GPIO.HIGH)
    GPIO.output(red_button, GPIO.HIGH)
    GPIO.output(yellow_button, GPIO.HIGH)

try:
    
    while True:

        setup()
            
        if GPIO.input(green_button) == GPIO.LOW:
            led_color(green_LED)

        if GPIO.input(blue_button) == GPIO.LOW:
            led_color(blue_LED)
            
        if GPIO.input(red_button) == GPIO.LOW:
            led_color(red_LED)
            
        if GPIO.input(blue_button) == GPIO.LOW:
            led_color(blue_LED)

        if GPIO.input(interupt) == GPIO.LOW:
            GPIO.output(interupt, GPIO.LOW)
            print(f"Pin {interupt} is turned OFF.")
            break
    
finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
