import RPi.GPIO as GPIO
import time

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc (num):
    sig = decimal2binary(num)
    GPIO.output(dac, sig)
    return sig


dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]

comp = 4

troyka = 17

maxVolt = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = 1)

GPIO.setup(comp, GPIO.IN)

try:
    while(True):
        for i in range (256):
            sig = adc(i)
            volt =( i / 256 )*maxVolt
            time.sleep(0.005)
            cmpVal = GPIO.input(comp)
            if cmpVal == 0:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(i,sig,volt))
                break


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()