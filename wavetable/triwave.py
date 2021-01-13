# Author: Emirhan Gocturk
# Description: Triangular wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, np.pi*2, 0.00156)
y = signal.sawtooth(t, 0.5)
plt.plot(t, y)  
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("Tri Wave Sample")
plt.show()

print("DATA DUMP= ", y)