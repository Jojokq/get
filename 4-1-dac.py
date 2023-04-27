def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
    
try:

    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)

    dac = [26,19,13,6,5,11,9,10]

    GPIO.setup(dac, GPIO.OUT)

    while(True):
        print("Enter an integer number between 0 and 255")
        inp = str(input())
        if inp == 'q':
            break
        elif is_digit(inp) == 0:
            print("ERROR: not a number")
        else:
            if inp.isdigit() == 0:
                if float(inp) < 0:
                    print("ERROR: number below zero")
                else:
                    print("ERROR: not an integer")
            else:
                decimal = int(inp)
                if decimal > 255:
                    print("ERROR: too big number")
                else:
                    print('Voltage: ', decimal/255 * 3.3 )
                    GPIO.output( dac, decimal2binary(decimal))




finally:
    GPIO.output(dac, 0)

    GPIO.cleanup()