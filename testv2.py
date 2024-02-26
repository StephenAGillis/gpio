import RPi.GPIO as GPIO
import time

# References GPIO pins by their physical pin numbers.
GPIO.setmode(GPIO.BCM)

def print_IO(x): # Print Digital Input/Output Pin(s)
    state = GPIO.gpio_function(x)
    print("pin state: ", x)
        
def print_Volts(x):
    voltage = "HIGH" if GPIO.input(x) else "Low"
    print("Pin voltage: ", x)

def set_high(x):
    print("set_high")
    for i in x:
        GPIO.output(i, GPIO.HIGH)
        state = GPIO.input(i)
        print(f"pin {i}'s state: {state} ")
        sleep()

def set_low(x):
    print("set_low")
    for i in x:
        GPIO.output(i, GPIO.LOW)
        state = GPIO.input(i)
        print(f"pin {i}'s state: {state} ")
        sleep()

def set_input(x):
    print("set_input")
    for i in x:
        GPIO.setup(i, GPIO.IN)
        mode = GPIO.gpio_function(i)
        print(f"pin {i}'s mode: IN") 
        sleep()

def set_output(x):
    print("set_output")
    for i in x:
        GPIO.setup(i, GPIO.OUT)
        mode = GPIO.gpio_function(i)
        print(f"pin {i}'s mode : OUT")
        sleep()

def power_row(x):
    pass

def sleep():
    time.sleep(2)

def set_state(x, pin):
    if x == "HIGH":
        GPIO.output(pin, GPIO.HIGH)
        sleep()
    if x == "LOW":
        GPIO.output(pin, GPIO.LOW)
        sleep()

leds = [{"pin": 13, "mode": GPIO.OUT, "value": GPIO.HIGH},
        {"pin": 19, "mode": GPIO.OUT, "value": GPIO.HIGH},
        {"pin": 26, "mode": GPIO.OUT, "value": GPIO.HIGH}]    # R G B settings

# Will be output, HIGH channels, top row to bottom row
rows = [{"pin": 18, "mode": GPIO.OUT, "value": GPIO.HIGH},
        {"pin": 23, "mode": GPIO.OUT, "value": GPIO.HIGH},
        {"pin": 24, "mode": GPIO.OUT, "value": GPIO.HIGH},
        {"pin": 25, "mode": GPIO.OUT, "value": GPIO.HIGH}]

cols = [{"pin": 12, "mode": GPIO.IN, "value": GPIO.LOW},
        {"pin": 16, "mode": GPIO.IN, "value": GPIO.LOW},
        {"pin": 20, "mode": GPIO.IN, "value": GPIO.LOW},
        {"pin": 21, "mode": GPIO.OUT, "value": GPIO.LOW}]    # left to right

leds = [13,19,26]
rows = [18,23,24,24]    # Top to bottom
cols = [12,16,20,21]     #left to right

try:
    for led in leds:
        pin = led
        mode = GPIO.OUT
        value = GPIO.HIGH
        
        GPIO.setup(pin, mode)
        GPIO.setup(pin, value)
        sleep()

    for led in leds:
        pin = led["pin"]
        mode = GPIO.LOW
        value = 
        GPIO.output(pin, mode)
        sleep()

    for led in leds:
        pin = led["pin"]
        mode = 
        value =

    
    
            
except KeyboardInterrupt:

    GPIO.cleanup()
#{"pin": 13, "mode": GPIO.OUT, "value": GPIO.HIGH}



