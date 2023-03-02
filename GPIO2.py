#task 1

import RPi.GPIO as GPIO
import time

channel = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)

GPIO.setup(channel, GPIO.OUT)
if GPIO.input(27) == 1:
    GPIO.output(channel, 1)
else:
    GPIO.output(channel, 0)

while(True):
    time.sleep(1)


GPIO.cleanup()

