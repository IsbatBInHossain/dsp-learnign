from assets import mysignals as sig
from matplotlib import style, pyplot as plt
import csv

input_signal = sig.InputSignal_1kHz_15kHz
impulse_signal = sig.Impulse_response

csvfile = 'conv_output.csv'


def calc_convolution(x, h):
    N = len(x)
    M = len(h)
    y = [0]*(N+M-1)

    for n in range(N+M-1):
        for k in range(N):
            if n-k >= 0 and n-k < M:
                y[n] += x[k] * h[n-k]
    return y


def write_csv(csvfile, output_arr):
    with open(csvfile, 'w') as output:
        writer = csv.writer(output, lineterminator=',')
        for i in output_arr:
            writer.writerow([i])


convolved_signal = calc_convolution(input_signal, impulse_signal)
write_csv(csvfile, convolved_signal)

style.use(['ggplot', 'dark_background'])
f, axs = plt.subplots(3, sharex=True)
f.suptitle('Convolution')

for ax, data, title in zip(axs, [input_signal, impulse_signal, convolved_signal], ['Input Signal', 'Impulse Response', 'Convolved Output Signal']):
    ax.plot(data, color='cyan' if title ==
            'Input Signal' else 'magenta' if title == 'Impulse Response' else 'red')
    ax.set_title(title)

plt.show()
