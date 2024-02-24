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
    GPIO.output(x, GPIO.HIGH)
    state = GPIO.input(x)
    print(f"pin {x}'s state: HIGH ")

def set_low(x):
    GPIO.output(x, GPIO.LOW)
    state = GPIO.input(x)
    print(f"pin {x}'s state: LOW ")

def set_input(x):
    GPIO.setup(x, GPIO.IN)
    mode = GPIO.gpio_function(x)
    print(f"pin {x}'s mode: IN") 

def set_output(x):
    GPIO.setup(x, GPIO.OUT)
    mode = GPIO.gpio_function(x)
    print(f"pin {x}'s mode : OUT")

led = [13, 19, 26] # R G B settings
rows = [18, 23, 24, 25] # top to bottom
cols = [12, 16, 20, 21] # left to right

# for i in range(len(led_pins)):

try:
    while True:
        for i in rows:
            set_output(i)

        break;
            
    
except KeyboardInterrupt:

    GPIO.cleanup()








