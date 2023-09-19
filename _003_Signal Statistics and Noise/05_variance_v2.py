from assets import mysignals as sig


def calc_mean(sig_arr):
    mean = 0.0
    for num in sig_arr:
        mean += num
    return mean/len(sig_arr)


def calc_variance(sig_arr):
    var = 0.0
    mean = calc_mean(sig_arr)
    for num in sig_arr:
        var += (num - mean)**2
    return var/len(sig_arr)


print(calc_variance(sig.InputSignal_1kHz_15kHz))
