import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

audio_file = 'tone.wav'

x, fs = sf.read(audio_file)

plt.subplot(3, 1, 1)
plt.plot(np.arange(8000), x[0:8000]); plt.ylabel('x(n)');
plt.subplot(3, 1, 2);
plt.plot(np.arange(1000), x[0:1000]); plt.ylabel('x(n)');
plt.subplot(3, 1, 3)
plt.stem(np.arange(100), x[0:100], '-.'); plt.ylabel('x(n)');
plt.xlabel('n \rightarrow');
plt.show()
