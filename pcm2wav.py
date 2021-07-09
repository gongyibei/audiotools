import os 
import numpy as np
import wave
import sys

path = sys.argv[1]
wav_path = sys.argv[1]
file_namelist = os.listdir(path)


pcm_list = []
for i in file_namelist:
    pcm_list.append(i)
#pcm_list.remove("mic.pcm")


for item in range(len(pcm_list)):
    pcm_path = path+pcm_list[item]
    wav_name = os.path.splitext(pcm_list[item])[0]
    wav_ =wav_path+wav_name+".wav"
    
    with open(pcm_path, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    with wave.open(wav_, 'wb') as wavfile:
        wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))#32000是采样率
        wavfile.writeframes(pcmdata)

