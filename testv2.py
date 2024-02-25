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
        print(f"pin {x}'s state: {state} ")

def set_low(x):
    print("set_low")
    for i in x:
        GPIO.output(i, GPIO.LOW)
        state = GPIO.input(i)
        print(f"pin {x}'s state: {state} ")

def set_input(x):
    print("set_input")
    for i in x:
        GPIO.setup(i, GPIO.IN)
        mode = GPIO.gpio_function(i)
        print(f"pin {x}'s mode: IN") 

def set_output(x):
    print("set_output")
    for i in x:
        GPIO.setup(i, GPIO.OUT)
        mode = GPIO.gpio_function(i)
        print(f"pin {x}'s mode : OUT")

def power_row(x):
    pass

def sleep():
    time.sleep(3)

def set_rows(x, row):
    if x == "HIGH":
        for i in row:
            GPIO.output(i, GPIO.HIGH)
    if x == "LOW":
        for i in row:
            GPIO.output(i, GPIO.LOW)

def set_leds(x, led):
    if x == "HIGH":
        for i in led:
            GPIO.output(i, GPIO.HIGH)
            sleep()
    if x == "LOW":
        for i in led:
            GPIO.output(i, GPIO.LOW)
            sleep()
    
leds = [13, 19, 26] # R G B settings
rows = [18, 23, 24, 25] # top to bottom
cols = [12, 16, 20, 21] # left to right

# for i in range(len(led_pins)):

try:
    set_output(leds)
    sleep()
    set_high(leds)
    sleep()
    set_low(leds)
    sleep()
    set_input(leds)
    
            
except KeyboardInterrupt:

    GPIO.cleanup()

    #while True:
     #   set_rows(HIGH, rows)
      #  for col in cols:
       #     set_low(col)
            






