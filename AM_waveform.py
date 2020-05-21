import matplotlib.pyplot as plt
import numpy as np
from math import pi
plt.close('all')
# Create Time axis
Fs = 2000;
n = np.arange(0,2,1/Fs)
# Generate Carrier wave
Fc = 50
Ac = 1
c = Ac*np.cos(2*pi*Fc*n) # Carrier wave
plt.subplot(3,1,1)
plt.plot(n,c); plt.title('Carrier')
plt.xlabel('Time(s)'); plt.ylabel('Amplitude');
plt.grid(True)
# Generate message signal
Fm = 2
Am = 0.5
m = Am*np.sin(2*pi*Fm*n) # message signal
plt.subplot(3,1,2)
plt.plot(n,m); plt.title('Information')
plt.xlabel('Time(s)'); plt.ylabel('Amplitude');
plt.grid(True)
# Amplitude modulated signal
s = c * (1 + m/Ac)
# plot
plt.subplot(3,1,3)
plt.plot(n,s); plt.title('Modulation Wave')
plt.xlabel('Time(s)'); plt.ylabel('Amplitude');
plt.grid(True)
plt.tight_layout()