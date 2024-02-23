import RPi.GPIO as GPIO
import time

# References GPIO pins by their physical pin numbers.
GPIO.setmode(GPIO.BCM)

def get_direction_and_state(pin_num):
    direction = "Out" if GPIO.gpio_function(pin_num) == GPIO.OUT else "In"
    state = GPIO.input(pin_num)
    return direction, state

def configure_pins():
    for num in array:
        GPIO.setup(num, GPIO.OUT)
        direction, state = get_direction_and_state(num)
        print(f"Pin # {num} is set to {direction}, state: {state}\n")
        time.sleep(1)

def set_high_and_low():
    for num in array:
        direction, state = get_direction_and_state(num)
        GPIO.output(num, GPIO.HIGH)
        direction, state = get_direction_and_state(num)
        print(f"Pin # {num} is set to {direction}, state: {state}\n")
        time.sleep(1)
        
        GPIO.output(num, GPIO.LOW)
        direction, state = get_direction_and_state(num)
        print(f"Pin # {num} is set to {direction}, state: {state}\n")
        time.sleep(1)

def set_reconfigure_pins():
    for num in array:
        GPIO.setup(num, GPIO.IN)
        direction, state = get_direction_and_state(num)
        print(f"Pin # {num} is set to {direction}, state: {state}\n")
        time.sleep(1)


array = [13,19,26]
value = 7

try:
    configure_pins()
    set_high_and_low()
    set_reconfigure_pins()

except KeyboardInterrupt:

    GPIO.cleanup()
