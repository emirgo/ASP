# Author: Emirhan Gocturk
# Description: Pulse wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, np.pi*2, 0.001534)
y = signal.square(t, 0.5)

index = 0
while index < len(y):
    y[index] = int(y[index])
    index += 1

plt.plot(t, y)  
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("Pulse Wave Sample")
plt.show()

print("DATA DUMP= ", y)
np.savetxt("wavetable\\datadumps\\pulsewave.txt", y, delimiter=',')