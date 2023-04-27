import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


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
    print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(nsig,sig,volt))
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
    nsig = 0
    data = []
    start_time = time.time()
    counter = 0
    while(nsig < 210):  #Use lower than 255 because of little amount of time
        nsig = adc(comp)
        volt = nsig /256 * 3.3
        leds_push(nsig)
        data.append(nsig)
        counter+=1
        

    GPIO.output(troyka, 0)



    while(nsig > 4):
        nsig = adc(comp)
        volt = nsig /256 * 3.3
        leds_push(nsig)
        data.append(nsig)
        counter+=1
        
    end_time = time.time() - start_time

    disc = counter/end_time
    
    plt.plot(data)
    plt.show()
    plt.savefig("AWESOME.png")
    
    






    data_str = [str(item) for item in data]
    print("время эксперимента  " + str(end_time) + "\nчастота дискретизации  " + str(disc) + "\nшаг квантования " + str(3.3/256) + "В")

    with open("data.txt", "w") as datafile:
        datafile.write("\n".join(data_str))
    with open("settings.txt", "w") as settingsfile:
        #settingsfile.write(str(start_time))
        settingsfile.write(str(3.3/256))
        settingsfile.write("\n")
        settingsfile.write(str(disc))

        


        
            


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()