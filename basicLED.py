import RPi.GPIO as GPIO
import time

# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin to use
pin_number = 21  # Change this to the desired pin number

# Set up the GPIO pin as an output
GPIO.setup(pin_number, GPIO.OUT)

try:
    # Turn the GPIO pin on
    GPIO.output(pin_number, GPIO.HIGH)
    print("Pin {} is turned ON.".format(pin_number))
    
    # Wait for 1 second
    time.sleep(1)
    
    # Turn the GPIO pin off
    GPIO.output(pin_number, GPIO.LOW)
    print("Pin {} is turned OFF.".format(pin_number))
    
finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
