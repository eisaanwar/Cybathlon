import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

dirPin = 11
speed1 = 3000  # Min pulse length out of 4096
speed2 = 2000

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dirPin, GPIO.OUT)
    GPIO.output(dirPin, GPIO.HIGH)
    pwm.set_pwm_freq(1500) #24 to 1526Hz

def move():
    while True:
        GPIO.output(dirPin, GPIO.HIGH) # set direction
        pwm.set_pwm(0, 0, speed1)
        time.sleep(3)
		pwm.set_pwm(0, 0, speed2)
		time.sleep(3)
    
def destroy(): # run when we press Ctrl-C
    pwm.set_pwm(0, 0, 0) # stop moving
    GPIO.output(dirPin, GPIO.LOW)
    GPIO.cleanup()

try:
    setup()
    print('Moving motor on channel 0, press Ctrl-C to quit...')
    move()
except KeyboardInterrupt: #CTRL+C pressed
    destroy() # switch off to exit

