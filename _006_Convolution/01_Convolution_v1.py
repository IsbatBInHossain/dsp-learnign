from matplotlib import style, pyplot as plt
from scipy import signal
from assets import mysignals as sig

style.use(['ggplot', 'dark_background'])

input_signal = sig.InputSignal_1kHz_15kHz
impulse_response = sig.Impulse_response
output_signal = signal.convolve(input_signal, impulse_response, mode='same')

titles = ['Input Signal', 'Impulse Response', 'Convolved Output Signal']

fig, axs = plt.subplots(3, sharex=True, figsize=(8, 6))
fig.suptitle('Convolution')

for ax, data, title in zip(axs, [input_signal, impulse_response, output_signal], titles):
    ax.plot(data, color='cyan' if title ==
            'Input Signal' else 'yellow' if title == 'Impulse Response' else 'magenta')
    ax.set_title(title)

plt.show()
