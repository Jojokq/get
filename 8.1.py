import matplotlib.pyplot as plt
import numpy as np

with open("settings.txt", 'r') as sts:
    settings = [float(i) for i in sts.read().split('\n')]

settings[1] = 1/settings[1]

data = np.loadtxt("data.txt", dtype=int)

data = settings[0] * data

ztime = data.max()
for i in range(8000):
    if ztime == data[i]:
        ztime = i
        break
ztime = settings[1]*ztime
rtime = len(data)*settings[1] - ztime
print(ztime, rtime)
time = np.linspace(0, settings[1] * len(data), len(data))

fig = plt.figure(figsize = (20, 10))

plt.plot(time, data, color = 'blue', marker = 'o', linewidth=0.4,  label = 'V(t)', markevery=440, markersize = 10.0)
    


plt.grid(True, which='major', linestyle='--')

plt.grid(True, which='minor', linestyle=':', )

plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.title("Процесс заряда и разряда конденсатора в RC-цепочке")
plt.text(40, 2.5, "время заряда = 22.2 c")
plt.text(40, 2.2, "время разряда = 41.3 c")
fig.legend()

plt.savefig('8.data.svg')
plt.show()




