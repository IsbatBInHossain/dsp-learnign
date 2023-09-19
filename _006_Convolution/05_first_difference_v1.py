from matplotlib import style, pyplot as plt
import numpy as np
from assets import mysignals as sig

first_diff = np.diff(sig.InputSignal_1kHz_15kHz)

style.use(['ggplot', 'dark_background'])

f, axs = plt.subplots(2, sharex=True)
f.suptitle("First difference")

for ax, data, title in zip(axs, [sig.InputSignal_1kHz_15kHz, first_diff], ['Input Signal', 'First difference']):
    ax.plot(data)
    ax.set_title(title)

plt.show()
