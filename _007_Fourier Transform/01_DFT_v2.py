from matplotlib import pyplot as plt, style
from assets import mysignals as sig
import cmath


def dft(x):
    N = int(len(x)/2)
    X_freq = [0.0] * N

    for k in range(N):
        X_freq[k] = sum(x[n] * cmath.exp(1j * 2 * cmath.pi * k * n / len(x))
                        for n in range(len(x)))

    return X_freq


freq_domain = dft(sig.InputSignal_1kHz_15kHz)
style.use('ggplot')

f, axs = plt.subplots(3, sharex=True)

f.suptitle('DFT')

titles = ['Input Signal',
          'Magnitude of Frequency Domain',
          'Phase of Frequency Domain']
signals = [sig.InputSignal_1kHz_15kHz,
           [abs(val) for val in freq_domain],  # Calculate magnitude
           [cmath.phase(val) for val in freq_domain]]  # Calculate phase

for ax, data, title in zip(axs, signals, titles):
    ax.plot(data)
    ax.set_title(title)

plt.show()
