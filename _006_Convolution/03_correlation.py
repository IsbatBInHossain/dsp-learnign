from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from assets import mysignals as sig

impulse_response = sig.Impulse_response
input_signal = sig.InputSignal_1kHz_15kHz

correlation_output = signal.correlate(
    input_signal, impulse_response, mode='same')
convolution_output = signal.convolve(
    input_signal, impulse_response, mode='same')

plt.plot(convolution_output, label='Convolution Output')
plt.plot(correlation_output, linestyle='--', label='Correlation Output')

plt.legend()
plt.show()
