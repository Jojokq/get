import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as pyplot
import numpy as np


dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4

troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = 1)

GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc (comp):
    sig = [0,0,0,0,0,0,0,0]
    nsig = 0
    
    for i in range (7, -1,-1):
        
        nsig+=2**i
        sig = decimal2binary(nsig)
        GPIO.output(dac, sig)
        time.sleep(0.0007)
        cmpVal = GPIO.input(comp)
        if cmpVal == 0:
            nsig-=2**i
        
    #volt = nsig/256*3.3
    return nsig

def leds_push(nsig):
    for i in range (0, 8):
        if 32 * (i - 1) < nsig:
            GPIO.output(leds[i], 1)
        else:
            GPIO.output(leds[i], 0)



try:
    volt = 0
    data = []
    start_t = time.clock()
    while(volt < 250):
        nsig = adc(comp)
        volt = nsig /256 * 3.3
        leds_push(nsig)
        time.sleep(0.05)
        


        
            


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()