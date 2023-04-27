def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)

    dac = [26,19,13,6,5,11,9,10]

    GPIO.setup(dac, GPIO.OUT)
    print("Введите период треугольного сигнала")
    timer = float(input())

    timer = timer/(256*2)

    while (True):
        for i in range (0,256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(timer)
        for i in range (254,-1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(timer)



finally:
    GPIO.output(dac, 0)

    GPIO.cleanup()