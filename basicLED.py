import RPi.GPIO as GPIO
import time

# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BCM)

# Buttons
blue_button= 10
green_button = 12
yellow_button = 21
red_button = 20

# LEDs
red_LED = 13
blue_LED = 26
green_LED = 19

interupt = 23

# Exit program
GPIO.setup(interupt, GPIO.OUT)

# Setup LEDs
GPIO.setup(green_LED, GPIO.OUT)
GPIO.setup(blue_LED, GPIO.OUT)
GPIO.setup(red_LED, GPIO.OUT)

# Setup buttons
GPIO.setup(green_button, GPIO.OUT)
GPIO.setup(blue_button, GPIO.OUT)
GPIO.setup(red_button, GPIO.OUT)
GPIO.setup(yellow_button, GPIO.OUT)


def mix_led(x,y):
    GPIO.output(x, GPIO.HIGH)
    GPIO.output(x, GPIO.HIGH)

    time.sleep(1)
    
    GPIO.output(x, GPIO.LOW)
    GPIO.output(x, GPIO.LOW)
    
def led_color(x):
    GPIO.output(x, GPIO.HIGH)
    
    time.sleep(1)
    
    GPIO.output(x, GPIO.LOW)
    print(f"Pin {x} is turned OFF.")


def set_HIGH():
    GPIO.output(interupt, GPIO.HIGH)
    GPIO.output(green_button, GPIO.HIGH)
    GPIO.output(blue_button, GPIO.HIGH)
    GPIO.output(red_button, GPIO.HIGH)
    GPIO.output(yellow_button, GPIO.HIGH)

try:

    set_HIGH()
    
    while True:
        
        if GPIO.input(green_button) == GPIO.LOW:
            led_color(green_LED)

        if GPIO.input(blue_button) == GPIO.LOW:
            led_color(blue_LED)
            
        if GPIO.input(red_button) == GPIO.LOW:
            led_color(red_LED)
            
        if GPIO.input(yellow_button) == GPIO.LOW:
            mix_led(red_LED, green_LED)

        if GPIO.input(interupt) == GPIO.LOW:
            GPIO.output(interupt, GPIO.LOW)
            print(f"Pin {interupt} is turned OFF.")
            break
    
finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
