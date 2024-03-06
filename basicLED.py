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

# Set up the GPIO pin as an output
GPIO.setup(green_button, GPIO.OUT)
GPIO.setup(green_LED, GPIO.OUT)

GPIO.setup(yellow_button, GPIO.OUT)

def green_light():
    GPIO.output(green_button, GPIO.HIGH)
    GPIO.output(green_LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(green_LED, GPIO.LOW)
    print(f"Pin {green_LED} is turned ON.")

try:
    
    while True:

        GPIO.output(yellow_button, GPIO.HIGH)
        GPIO.output(green_button, GPIO.HIGH)
        
        if GPIO.input(yellow_button) == GPIO.LOW:
            GPIO.output(green_LED, GPIO.LOW)
            print(f"Pin {green_LED} is turned OFF.")
            break
            
        if GPIO.input(green_button) == GPIO.LOW:
            green_light()

    
finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
