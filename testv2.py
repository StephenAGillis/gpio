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
    GPIO.output(i, GPIO.HIGH)
    state = GPIO.input(i)
    print(f"pin {i}'s state: {state} ")
    sleep()

def set_low(x):
    print("set_low")
    GPIO.output(i, GPIO.LOW)
    state = GPIO.input(i)
    print(f"pin {i}'s state: {state} ")
    sleep()

def set_input(x):
    print("set_input")
    GPIO.setup(i, GPIO.IN)
    mode = GPIO.gpio_function(i)
    print(f"pin {i}'s mode: IN") 
    sleep()

def set_output(x):
    print("set_output")
    GPIO.setup(i, GPIO.OUT)
    mode = GPIO.gpio_function(i)
    print(f"pin {i}'s mode : OUT")
    sleep()


def sleep():
    time.sleep(2)

#      12   16   20   21
#  18  [1]  [2]  [3]  [A]
#  23  [4]  [5]  [6]  [B]
#  24  [7]  [8]  [9]  [C]
#  25  [*]  [0]  [#]  [D]

def find_index(x,y):
    if x == 18 and y == 12:
        print("button 1 is pushed")
        GPIO.setup(13, GPIO.OUT)
        GPIO.output(13, GPIO.HIGH)
        sleep()
        GPIO.setup(13, GPIO.IN)
    if x == 18 && y == 16:
        pass
    if x == 18 && y == 20:
        pass
    

leds = [13,19,26]
rows = [18,23,24,24]    # Top to bottom
cols = [12,16,20,21]     #left to right


try:
    while True:
        for i in rows:
            GPIo.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        
            for j in cols:
                GPIO.setup(j, GPIO.IN)
                if GPIO.input(j) == GPIO.HIGH:
                    find_index(i,j)
            GPIO.output(i, GPIO.LOW)
            GPIO.setup(i, GPIO.IN)
    

except KeyboardInterrupt:

    GPIO.cleanup()
#{"pin": 13, "mode": GPIO.OUT, "value": GPIO.HIGH}



