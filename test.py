import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# (digit#)port#    ::    (1)port5, (2)port13, (3)port19, (4)port26
d1 = 5
d2 = 13
d3 = 19
d4 = 26

def set_seq1(a,b,c,d):
    
    GPIO.output(a, GPIO.HIGH)
    GPIO.output(b, GPIO.LOW)
    GPIO.output(c, GPIO.LOW)
    GPIO.output(d, GPIO.HIGH)
    time.sleep(1)
    
def set_seq2(a,b,c,d):
    
    GPIO.output(a, GPIO.LOW)
    GPIO.output(b, GPIO.LOW)
    GPIO.output(c, GPIO.HIGH)
    GPIO.output(d, GPIO.HIGH)
    time.sleep(1)

def set_seq3(a,b,c,d):
    
    GPIO.output(a, GPIO.LOW)
    GPIO.output(b, GPIO.HIGH)
    GPIO.output(c, GPIO.HIGH)
    GPIO.output(d, GPIO.LOW)
    time.sleep(1)
    
def set_seq4(a,b,c,d):
    
    GPIO.output(a, GPIO.HIGH)
    GPIO.output(b, GPIO.HIGH)
    GPIO.output(c, GPIO.LOW)
    GPIO.output(d, GPIO.LOW)
    time.sleep(1)

def setup_ports(a,b,c,d):
    GPIO.setup(a, GPIO.OUT)
    GPIO.setup(b, GPIO.OUT)
    GPIO.setup(c, GPIO.OUT)
    GPIO.setup(d, GPIO.OUT)

try:
    counter = 0   
    
    setup_ports(d1,d2,d3,d4)
    
    while counter <= 20:
        set_seq1(d1,d2,d3,d4)
        set_seq2(d1,d2,d3,d4)
        set_seq3(d1,d2,d3,d4)
        set_seq4(d1,d2,d3,d4)
        counter += 1
        
    set_low(d1,d2,d3,d4)

finally:
    GPIO.cleanup()
    
