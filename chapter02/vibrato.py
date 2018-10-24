import numpy as np

def vibrato(x, fs, ModFreq, Width):
    ya_alt = 0
    Delay = Width

    DELAY = np.round_(Delay * fs)
    WIDTH = np.round_(Width * fs)
    if WIDTH > DELAY:
        print('delay greater than basic delay !!!')
        return

    MODFREQ = ModFreq / fs
    LEN = x.size
    L = int(2 + DELAY + WIDTH * 2)
    DelayLine = np.zeros((L, 1), dtype=float)
    y = np.zeros((x.size, 1), dtype=float)
    for n in np.arange(x.size - 1):
        M = MODFREQ
        MOD = np.sin(M*2*np.pi*n)
        TAP = 1 + DELAY + WIDTH*MOD
        i = np.floor(TAP)
        frac = TAP - i
        DelayLine = np.append(x[n], DelayLine[:L-1])
        y[n] = DelayLine[int(i)+1] * frac + DelayLine[int(i)]*(1-frac)
        # print('%d -- %f' % (n, y[n]))

    return y