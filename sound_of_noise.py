import numpy as np
import sounddevice as sd
from scipy import signal

duration = 5.0  # Duration of the generated noise in seconds
fs = 44100  # Sampling frequency in Hz
samples = int(duration*fs)

# Generate white noise
white_noise = np.random.normal(0, 1, int(duration * fs))

# Generate pink noise

# Generate pink noise
pink_noise = np.random.randn(samples)
pink_noise = np.cumsum(pink_noise)
pink_noise /= np.max(np.abs(pink_noise))

# Generate blue noise

# Apply a high-pass filter to the white noise
cutoff_freq = 1000  # Cutoff frequency in Hz
b, a = signal.butter(4, cutoff_freq / (fs / 2), 'high')
blue_noise = signal.lfilter(b, a, white_noise)
blue_noise /= np.max(np.abs(blue_noise))

# Generate brown noise

# Generate brown noise by cumulative sum of white noise
brown_noise = np.cumsum(white_noise)
brown_noise /= np.max(np.abs(brown_noise))

# Generate dark noise
dark_noise = np.random.standard_normal(int(duration * fs))

# Generate shot noise 
shot_noise = np.random.poisson(1.0, int(duration * fs)) - 1.0

# Generate thermal noise
thermal_noise = np.random.normal(0, 1, int(duration * fs))

violet_noise = np.cumsum(np.random.randn(samples)) * np.sqrt(fs)

# Scale the noise to an audible level
scale_factor = 0.1

noise_list = [white_noise , pink_noise , blue_noise , brown_noise , dark_noise , shot_noise , thermal_noise , violet_noise]

# Play the white noise
print("Playing white noise...")
sd.play(white_noise*scale_factor, fs)
sd.wait()

# Play the violet noise
print("Playing violet noise...")
sd.play(violet_noise*0.5, fs)
sd.wait()

# Play the pink noise
print("Playing pink noise...")
sd.play(pink_noise*4.6, fs)
sd.wait()

# Play the shot noise
print("Playing shot noise...")
sd.play(shot_noise*scale_factor/10, fs)
sd.wait()

# Play the thermal noise
print("Playing thermal noise...")
sd.play(thermal_noise*scale_factor/10, fs)
sd.wait()

# Play the blue noise
print("Playing blue noise...")
sd.play(blue_noise*scale_factor, fs)
sd.wait()

# Play the brown noise
print("Playing brown noise...")
sd.play(brown_noise*1.5, fs)
sd.wait()

# Play the dark noise
print("Playing dark noise...")
sd.play(dark_noise*0.1/100, fs)
sd.wait()