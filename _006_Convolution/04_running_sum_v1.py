from matplotlib import style, pyplot as plt
from numpy import cumsum
from assets import mysignals as sig

running_sum = cumsum(sig.InputSignal_1kHz_15kHz)

style.use(['ggplot', 'dark_background'])

f, axs = plt.subplots(2, sharex=True)
f.suptitle("Running Sum")

for ax, data, title in zip(axs, [sig.InputSignal_1kHz_15kHz, running_sum], ['Input Signal', 'Running Sum']):
    ax.plot(data)
    ax.set_title(title)

plt.show()
