import os
import numpy as np
import sys





def wav2pcm(wavfile,pcmfile,data_type=np.int16):
    f = open(wavfile,"rb")
    #print(f)
    f.seek(0)
    f.read(44)
    data = np.fromfile(f,dtype=data_type)
    data.tofile(pcmfile)



def main_wav2pcm(wavpath):

    item_wavpath = wavpath+".wav"
    item_pcmpath = wavpath+".pcm"
    wav2pcm(wavfile=item_wavpath,pcmfile=item_pcmpath)




def main():

    wav_path = sys.argv[1]
    main_wav2pcm(wav_path)



if __name__ == "__main__":
    main()