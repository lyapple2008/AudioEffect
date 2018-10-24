import numpy as np

fs = 44100
fc = 8000
K = np.tan(np.pi * fc / fs)

print('            b0         b1         a1')
print('Lowpass     %f          %f        %f' % (K/(K+1), K/(K+1), (K-1)/(K+1)))
print('Highpass    %f          %f        %f' % (1/(K+1), -1/(K+1), (K-1)/(K+1)))
print('Allpass     %f          %f        %f' % ((K-1)/(K+1), 1, (K-1)/(K+1)))