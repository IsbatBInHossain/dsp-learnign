from assets import mysignals as sig


def calc_mean(sig_arr):
    mean = 0.0
    for num in sig_arr:
        mean += num
    return mean/len(sig_arr)


def calc_std(sig_arr):
    std = 0.0
    mean = calc_mean(sig_arr)
    for num in sig_arr:
        std += (num - mean)**2
    return (std/len(sig_arr))**0.5


print(calc_std(sig.InputSignal_1kHz_15kHz))
