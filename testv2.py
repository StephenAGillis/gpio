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
    for num in x:
        GPIO.setup(num, GPIO.OUT)
        get_direction_and_state(num)
        time.sleep(1)

def disable_pins(x):
    print("Entered disable_pins loop")
    for num in x:
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

def establish_rows(x)
    for num in x:
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)
        time.sleep(1)

def establish_cols(x)
    for num in x:
        GPIO.setup(x,GPIO.IN) 

def set_pin_input(x):
    GPIO.setup(x, GPIO.IN)
    time.sleep(1)
    
def set_pin_output(x):
    GPIO.setup(x, GPIO.OUT)
    time.sleep(1)
    
led_pins = [13, 19, 26]
rows = [18, 23, 24, 25] # top to bottom
cols = [12, 16, 20, 21] # left to right

try:
    configure_pins(led_pins)
    establish_rows(rows)
    establish_cols(cols)

    while True:
        for num in rows:
            GPIO.output(num, GPIO.HIGH)
            for num in cols:
                GPIO.input(num, GPIO.IN)
                if GPIO.input(12, GPIO.IN) == GPIO.HIGH:
                    if GPIO.output(18, GPIO.HIGH):
                        set_led_color(13) 
                        
    disable_pins(rows)
    disable_pins(cols)
    disable_pins(led_pins)
    
except KeyboardInterrupt:

    GPIO.cleanup()



   12  16  20  21    (columns)
18
23
24
25
(rows)

setup

loop through each row
    set row to 5v
    loop though each each column which is set to LOW
        if column goes HIGH
            perform action
            set back to low
            continue 
    set row to 0v





















