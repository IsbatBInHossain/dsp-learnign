from matplotlib import pyplot as plt, style
from assets import mysignals as sig
import math


def dft(x):
    N = int(len(x)/2)
    X_real = [0] * N
    X_img = [0] * N
    X_mag = [0.0] * N

    for k in range(N):
        for n in range(len(x)):
            X_real[k] += x[n] * math.cos(2*math.pi * k*n/len(x))
            X_img[k] -= x[n] * math.sin(2*math.pi * k*n/len(x))
            X_mag[k] = math.sqrt(X_real[k]**2 + X_img[k]**2)

    return X_real, X_img, X_mag


def idft(X_real, X_imag):
    N = len(X_real)
    x = [0.0] * (2*N)

    for k in range(N):
        for n in range(2*N):
            angle = 2 * math.pi * k * n / (2*N)
            x[n] += (1/N) * (X_real[k] * math.cos(angle) -
                             X_imag[k] * math.sin(angle))

    return x


input_signal = sig.ecg_signal
freq_real, freq_img, freq_mag = dft(input_signal)
time_domain_signal = idft(freq_real, freq_img)

f, axs = plt.subplots(5, sharex=True)

f.suptitle('IDFT of ECG signal')

titles = ['ECG Input Signal',
          'Frequency Domain (Real)', 'Freqency Domain (Imaginary)', 'Frequency Domain (Magnitude)', 'Time Domain (IDFT)']
signals = [input_signal, freq_real, freq_img, freq_mag, time_domain_signal]

for ax, data, title in zip(axs, signals, titles):
    ax.plot(data)
    ax.set_title(title)


plt.show()
