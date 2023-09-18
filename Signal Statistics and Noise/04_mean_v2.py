from assets import mysignals as sig

src_signal = sig.InputSignal_1kHz_15kHz


def calc_mean(sig_arr):
    mean = 0.0
    for i in sig_arr:
        mean += i
    return mean/len(sig_arr)


print(calc_mean(src_signal))
