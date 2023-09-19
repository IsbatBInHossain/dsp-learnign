from matplotlib import style, pyplot as plt
from assets import mysignals as sig

style.use('dark_background')
input_signal = sig.InputSignal_1kHz_15kHz


def calc_running_sum(input_signal):
    running_sum = [0]*len(input_signal)
    cum_sum = 0
    for i in range(len(input_signal)):
        cum_sum += input_signal[i]
        running_sum[i] = cum_sum
    return running_sum


running_sum = calc_running_sum(input_signal)

f, axs = plt.subplots(2, sharex=True)
f.suptitle("Running Sum")

for ax, data, title in zip(axs, [input_signal, running_sum], ['Input Signal', 'Running Sum']):
    ax.plot(data)
    ax.set_title(title)

plt.show()
