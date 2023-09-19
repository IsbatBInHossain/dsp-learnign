from scipy import signal
import numpy as np

sig = np.array([0, 0, 1, 2, 0, 1, 2, 1, 0])
_filter = np.array([1, 1, 0, 1])

convolution_output = signal.convolve(sig, _filter)
print(f'Convolution result: {convolution_output}')
deconvolution_output = signal.deconvolve(convolution_output, _filter)
print(f'Convolution result: {deconvolution_output}')
