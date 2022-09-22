#button debounce v1.0
import time
import RPi.GPIO as GPIO

# pin numbers mapped to breakout board
# BCM - Broadcom chip-specific pin number, "GPIO"
#GPIO.setmode(GPIO.BCM) 	

def setup():
# pin numbers mapped to board pins on GPIO header
GPIO.setmode(GPIO.BOARD) # select board numbering scheme
switchPin = 18	# pin number on GPIO header, can change
GPIO.setup(switchPin, GPIO.IN) # set pin as input

prev_input_state = 0 # record previous pin state

def readPin():
	while True:
		time.sleep(0.04) # polling rate 25Hz
		input = GPIO.input(switchPin)	# read pin state
		#if the previous state was low and now it is high
		#i.e. switch was open, and now it is closed
		if((not prev_input_state) and input)
		print("Button pressed")
		#update previous state
		prev_input_state = input
		#add delay to debounce button
		time.sleep(0.05) # 50 ms delay
def destroy():
	GPIO.cleanup() #Garbage collector
try:
	setup()
	print("Reading pin state...press Ctrl-C to quit")
	readPin()
except KeyboardInterrupt: # if key event
    destroy() # end program
