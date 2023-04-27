import RPi.GPIO as GPIO
import time

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc (comp):
    sig = [0,0,0,0,0,0,0,0]
    nsig = 0
    for i in range (7, 0,-1):
        
        nsig+=2**i
        sig = decimal2binary(nsig)
        GPIO.output(dac, sig)
        time.sleep(0.0007)
        cmpVal = GPIO.input(comp)
        if cmpVal == 0:
            nsig-=2**i
        
    volt = nsig/256*3.3
    print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(nsig,sig,volt))
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
        sig = adc(comp)
        
            


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()