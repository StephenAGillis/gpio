import RPi.GPIO as GPIO
import time

# References GPIO pins by their physical pin numbers.
GPIO.setmode(GPIO.BCM)

def get_direction_and_state(x):
    direction = "Out" if GPIO.gpio_function(x) == GPIO.OUT else "In"
    state = GPIO.input(x)
    print(f"Pin # {x} is set to {direction}, state: {state}")

def configure_pins(x):
    print("Entered configure_pins loop")
    for num in pins:
        GPIO.setup(num, GPIO.OUT)
        get_direction_and_state(num)
        time.sleep(1)

def disable_pins():
    print("Entered disable_pins loop")
    for num in pins:
        GPIO.setup(num, GPIO.IN)
        get_direction_and_state(num)
        time.sleep(1)
        
def set_high_and_low(x):
    print("Entered set_high_and_low loop")
    for num in x:
        GPIO.output(num, GPIO.HIGH)
        time.sleep(1)

        get_direction_and_state(num)
        
        GPIO.output(num, GPIO.LOW)
        time.sleep(1)

def set_led_color(x):
    GPIO.output(x, GPIO.HIGH)
    time.sleep(1)
    
    GPIO.output(x, GPIO.LOW)
    time.sleep(1)

def set_pin_input(x):
    GPIO.setup(x, GPIO.IN)
    time.sleep(1)

def set_pin_output(x):
    GPIO.setup(x, GPIO.OUT)
    time.sleep(1)
    
pins = [13, 19, 26]

try:
    configure_pins()
    set_high_and_low(pins)
    disable_pins()
    
except KeyboardInterrupt:

    GPIO.cleanup()
