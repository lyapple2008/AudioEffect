import numpy as np
import soundfile as sf
from vibrato import vibrato

audio_file = '../chapter01/tone.wav' # 'voiceSrc.wav'
x, fs = sf.read(audio_file)
ModFreq = 4
Width = 0.005

y = vibrato(x, fs, ModFreq, Width)

audio_vibrato = 'voiceSrc_vibrato.wav'
sf.write(audio_vibrato, y, fs)