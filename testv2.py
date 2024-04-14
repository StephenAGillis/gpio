import RPi.GPIO as GPIO
from time import sleep

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pins for the ULN2003 driver
IN1 = 5
IN2 = 13
IN3 = 19
IN4 = 26

# Set up the GPIO
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Function to rotate the stepper motor one step
def step(delay, step_sequence):
    for i in range(4):
        GPIO.output(IN1, step_sequence[i][0])
        GPIO.output(IN2, step_sequence[i][1])
        GPIO.output(IN3, step_sequence[i][2])
        GPIO.output(IN4, step_sequence[i][3])
        sleep(delay)

# Function to move the stepper motor one step forward
def step_forward(delay, steps):
    for _ in range(steps):
        step(delay, [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]])

# Function to move the stepper motor one step backward
def step_backward(delay, steps):
    for _ in range(steps):
        step(delay, [[0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1]])

try:
    delay = 0.005  # Adjust this value for the delay between steps
    while True:
        # Rotate one revolution forward (clockwise)
        step_forward(delay, 100)
        # Pause for 2 seconds
        sleep(2)
        # Rotate one revolution backward (counterclockwise)
        step_backward(delay, 100)
        # Pause for 2 seconds
        sleep(2)

except KeyboardInterrupt:
    print("\nExiting the script.")
    GPIO.cleanup()
