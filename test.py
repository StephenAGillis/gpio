import RPi.GPIO as GPIO
import time

# References GPIO pins by their physical pin numbers.
GPIO.setmode(GPIO.BCM)

def get_direction_and_state(pin_num):
    direction = "Out" if GPIO.gpio_function(pin_num) == GPIO.OUT else "In"
    state = GPIO.input(pin_num)
    return direction, state

try:

    array = [13,19,26]

    # Configure pins, set to output
    for num in array:
        GPIO.setup(num, GPIO.OUT)
        direction, state = get_direction_and_state(num)
        print(f"Pin # {num} is set to {direction}, state: {state}\n")
        time.sleep(1)

    # Set to HIGH or LOW
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

    # Set pins back to input
    for num in array:
        GPIO.setup(num, GPIO.IN)
        direction, state = get_direction_and_state(num)
        print(f"Pin # {num} is set to {direction}, state: {state}\n")
        time.sleep(1)

except KeyboardInterrupt:

    GPIO.cleanup()
# test 2

