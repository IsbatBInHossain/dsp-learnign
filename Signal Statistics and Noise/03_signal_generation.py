from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal
import numpy as np

t = np.linspace(0, 1.0, 20001)

# Signal = amp * sin(2 * pi * f)

sig_5Hz = np.sin(2 * np.pi * 5 * t)
sig_250Hz = np.sin(2 * np.pi * 250 * t)
sig_5Hz_250Hz = sig_5Hz + sig_250Hz

f, ax = plt.subplots(3, sharex=True)
f.suptitle("Signals")
ax[0].plot(sig_5Hz)
ax[0].set_title('5 Hz signal')
ax[1].plot(sig_250Hz)
ax[1].set_title('250 Hz signal')
ax[2].plot(sig_5Hz_250Hz)
ax[2].set_title('5 Hz signal + 250 Hz signal')
plt.show()
