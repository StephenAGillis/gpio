import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# (digit#)port#    ::    (1)port5, (2)port13, (3)port19, (4)port26
d1 = 5
d2 = 13
d3 = 19
d4 = 26

def set_seq(a,b,c,d):
    GPIO.output(a, GPIO.HIGH)
    GPIO.output(a, GPIO.HIGH)
    GPIO.output(a, GPIO.HIGH)
    GPIO.output(a, GPIO.HIGH)

def setup_ports(a,b,c,d)
    GPIO.setup(a, GPIO.OUT)
    GPIO.setup(b, GPIO.OUT)
    GPIO.setup(c, GPIO.OUT)
    GPIO.setup(d, GPIO.OUT)

def set_low(a,b,c,d)
    GPIO.output(a, GPIO.LOW)
    GPIO.output(b, GPIO.LOW)
    GPIO.output(c, GPIO.LOW)
    GPIO.output(d, GPIO.LOW)

try:
    setup_ports(d1,d2,d3,d4)
    time.sleep(1)
    set_seq(d1,d2,d3,d4)
    time.sleep(1)
    set_low(d1,d2,d3,d4)

finally:
    GPIO.cleanup()
    
