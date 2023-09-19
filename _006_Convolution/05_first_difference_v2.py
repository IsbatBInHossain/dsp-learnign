from matplotlib import style, pyplot as plt
from assets import mysignals as sig


def calc_first_diff(input_signal):
    first_diff = [0]*(len(input_signal)-1)
    first_diff[0] = 0
    for i in range(1, len(input_signal)):
        first_diff[i-1] = input_signal[i] - input_signal[i-1]
    return first_diff


style.use('dark_background')
input_signal = sig.InputSignal_1kHz_15kHz
first_diff = calc_first_diff(input_signal)

f, axs = plt.subplots(2, sharex=True)
f.suptitle("First difference")

for ax, data, title in zip(axs, [input_signal, first_diff], ['Input Signal', 'First Difference']):
    ax.plot(data)
    ax.set_title(title)

plt.show()
