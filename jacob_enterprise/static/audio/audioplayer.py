import sounddevice as sd
from scipy.io import wavfile
import numpy as np 

def play_wav_file(file_path):
    # Read the WAV file
    samplerate, data = wavfile.read(file_path)
    
    # Normalize data if necessary
    if data.dtype != 'float32':
        # Normalize data to float32 if it’s not already
        data = data / np.max(np.abs(data), axis=0)  # Normalize to [-1, 1]
        data = data.astype(np.float32)  # Convert to float32

    # Play the sound
    sd.play(data, samplerate)
    sd.wait()  # Wait until the sound has finished playing

# Call the function with the path to your WAV file
play_wav_file('C:/Users/jasmi/OneDrive/Documents/Zoom/welcome.wav')
