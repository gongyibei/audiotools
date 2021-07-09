import wave 
import os
import numpy as np


def stereo2mono(input_path, output_dir):
    """
    :param input_path: 待处理音频的路径
    :param output_dir: 输出音频的目录
    """
    with  wave.open(input_path, 'rb') as f:
        framerate = f.getframerate()
        nframes = f.getnframes()
        nchannels = f.getnchannels()
        sampwidth = f.getsampwidth()
        frames = f.readframes(nframes)

    frames = np.array(bytearray(frames))
    frames = frames.reshape([480000,6])
    left = frames[:,:3].reshape([1440000])
    right = frames[:,3:].reshape([1440000])
        
    basename = os.path.basename(input_path)[:-4]
    
    with wave.open('{}/{}_{}.wav'.format(output_dir, basename, 'left'), 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.writeframes(bytes(left))
         
    with wave.open('{}/{}_{}.wav'.format(output_dir, basename, 'right'), 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.writeframes(bytes(right))

        
stereo2mono('./stereo.wav', '.')
