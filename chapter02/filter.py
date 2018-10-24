import numpy as np

def aplowpass(x, Wc):
    c = (np.tan(np.pi * Wc/2) - 1) / (np.tan(np.pi*Wc/2) + 1)
    xh = 0
    y = np.array([])
    for n in np.arange(x.size()):
        xh_new = x[n] - c * xh
        ap_y = c * xh_new + xh
        xh = xh_new
        y = np.append(y, 0.5 * (x[n] + ap_y))

    return y