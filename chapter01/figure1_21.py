import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
import soundfile as sf

audio_file = 'tone.wav'

x, fs = sf.read(audio_file)
f, t, Sxx = signal.spectrogram(x, fs, nfft=1024)
plt.pcolormesh(t, f[0:20], Sxx[0:20])
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


Pxx, freqs, bins, im = plt.specgram(x, NFFT=1024, Fs=fs)
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, 0, 1000))
plt.show()