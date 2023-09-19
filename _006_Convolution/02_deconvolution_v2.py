from matplotlib import style, pyplot as plt
from scipy import signal
import numpy as np
from assets import mysignals as sig

style.use(['ggplot', 'dark_background'])
input_signal = sig.InputSignal_1kHz_15kHz
impulse_response = sig.Impulse_response

convolution_output = signal.convolve(
    input_signal, impulse_response, mode='full')

deconvolution_output, _ = signal.deconvolve(
    convolution_output, impulse_response)

titles = ['Input signal', 'Impulse Response',
          'Convolved Signal', 'Deconvolved Signal']
signal_data = [input_signal, impulse_response,
               convolution_output, deconvolution_output]

f, axs = plt.subplots(4, sharex=True, figsize=(8, 10))
f.suptitle('Deconvolution')

for ax, data, title in zip(axs, signal_data, titles):
    ax.plot(data)
    ax.set_title(title)

plt.tight_layout()
plt.show()
