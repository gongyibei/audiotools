import wave 
import os

def add_blank(file_name, save_path, n):

    with wave.open(file_name, 'rb') as f:
        framerate = f.getframerate()
        nframes = f.getnframes()
        nchannels = f.getnchannels()
        sampwidth = f.getsampwidth()
        frames = f.readframes(nframes)

    base_name = os.path.basename(file_name)[:-4]
    save_name = f'{save_path}{base_name}+{n}.wav'
    with wave.open(save_name, 'wb') as fo:
        fo.setnchannels(nchannels)
        fo.setsampwidth(sampwidth)
        fo.setframerate(framerate)
        fo.writeframes(b'0x00'*n)
        fo.writeframes(frames)

add_blank('./sample-000000.wav', './', 1)
