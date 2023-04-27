import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(22 , 1000)

try:
    while True:
        print("enter duty cycle")
        dutycycle = float(input())
        p.start(dutycycle)
        time.sleep(30)
        p.stop()




finally:
    GPIO.output(22, 0)
    GPIO.cleanup()