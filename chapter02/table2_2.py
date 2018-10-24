import numpy as np

fs = 44100
fc = 8000
K = np.tan(np.pi * fc / fs)
Q = 1 / np.sqrt(2)

print('            b0    b1    b2    a1    a2')
print('Lowpass     %f    %f    %f    %f    %f' % (K*K*Q/(K*K*Q+K+Q), 2*K*K*Q/(K*K*Q+K+Q), K*K*Q/(K*K*Q+K+Q), 2*Q*(K*K-1)/(K*K*Q+K+Q), (K*K*Q-K+Q)/(K*K*Q+K+Q)))
print('Highpass    %f    %f    %f    %f    %f' % (Q/(K*K*Q+K+Q), -2*Q/(K*K*Q+K+Q), Q/(K*K*Q+K+Q), 2*Q*(K*K-1)/(K*K*Q+K+Q), (K*K*Q-K+Q)/(K*K*Q+K+Q)))
print('Allpass     %f    %f    %f    %f    %f' % ((K*K*Q-K+Q)/(K*K*Q+K+Q), 2*Q*(K*K-1)/(K*K*Q+K+Q), 1, 2*Q*(K*K-1)/(K*K*Q+K+Q), (K*K*Q-K+Q)/(K*K*Q+K+Q)))