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

def set_led_color(pin):
    state = GPIO.input(pin)
    
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)

    print(f"State = {state}\n") 
    
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

def pin_input(pin):
    GPIO.setup(pin, GPIO.IN)
    time.sleep(1)

def pin_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    time.sleep(1)
  
def pin_state(pin):
    state = GPIO.input(pin)
    print(f"State = {state}\n")  
    time.sleep(1)
    
def full_test():
    configure_pins()
    set_high_and_low()
    set_reconfigure_pins()


GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

try:
  pin_state(13)
  pin_output(13)
  set_led_color(13)
  pin_state(13)
  pin_input(13)
  pin_state(13)

except KeyboardInterrupt:

    GPIO.cleanup()
