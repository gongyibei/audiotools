import os 
import numpy as np
import wave
import sys

path = sys.argv[1]
wav_path = sys.argv[2]



with open(path, 'rb') as pcmfile:
    pcmdata = pcmfile.read()
with wave.open(wav_path, 'wb') as wavfile:
    wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))#32000是采样率
    wavfile.writeframes(pcmdata)

