import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
duration = 2.0  # Duration of the generated noise in seconds
fs = 64e3   # Sampling frequency in Hz

# Generate white noise
white_noise = np.random.randn(int(duration * fs))

# Generate shot noise
shot_noise = np.random.poisson(0.1, int(duration * fs))

# Generate pink noise
pink_noise = np.random.randn(int(duration * fs))
pink_noise = np.cumsum(pink_noise)
pink_noise -= np.mean(pink_noise)

# Generate flicker noise
flicker_noise = np.random.randn(int(duration * fs))
flicker_noise = np.cumsum(flicker_noise)
flicker_noise -= np.mean(flicker_noise)

# Generate thermal noise
thermal_noise = np.random.randn(int(duration * fs))

# Generate burst noise
burst_noise = np.random.randint(-1, 2, int(duration * fs))

# Generate orange noise
orange_noise = np.random.randn(int(duration * fs))
orange_noise = np.cumsum(orange_noise)
orange_noise -= np.mean(orange_noise)

# Generate blue noise
blue_noise = np.random.randn(int(duration * fs))
blue_noise = np.cumsum(blue_noise)
blue_noise -= np.mean(blue_noise)

# Generate purple noise
purple_noise = np.random.randn(int(duration * fs))
purple_noise = np.cumsum(purple_noise)
purple_noise -= np.mean(purple_noise)

# Generate brown noise
brown_noise = np.random.randn(int(duration * fs))
brown_noise = np.cumsum(brown_noise)
brown_noise -= np.mean(brown_noise)

# Generate green noise
green_noise = np.random.randn(int(duration * fs))
green_noise = np.cumsum(green_noise)
green_noise -= np.mean(green_noise)

# Generate dark noise
dark_noise = np.random.randn(int(duration * fs))
dark_noise = np.cumsum(dark_noise)
dark_noise -= np.mean(dark_noise)

# Set plot style with black background
plt.style.use('dark_background')

# Create subplots for noise images and spectrograms
fig, axes = plt.subplots(3, 4, figsize=(14, 15))
fig.subplots_adjust(left=0.1, hspace=0.3, wspace=0.5)

noises = [
    (white_noise, "White Noise"),
    (shot_noise, "Shot Noise"),
    (pink_noise, "Pink Noise"),
    (flicker_noise, "Flicker Noise"),
    (thermal_noise, "Thermal Noise"),
    (burst_noise, "Burst Noise"),
    (orange_noise, "Orange Noise"),
    (blue_noise, "Blue Noise"),
    (purple_noise, "Purple Noise"),
    (brown_noise, "Brown Noise"),
    (green_noise, "Green Noise"),
    (dark_noise, "Dark Noise"),
]

for i, (noise, title) in enumerate(noises):

   
    # Calculate and plot spectrogram
    f, t, Sxx = signal.spectrogram(noise, fs=fs, window='hann', nperseg=256, noverlap=128)
    ax_spec = axes[i // 4, i % 4]
    pcm = ax_spec.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto', cmap='jet')
    ax_spec.set_ylabel('Frequency (Hz)')
    ax_spec.set_ylim(0, fs/2)  # Limit the frequency range
    ax_spec.spines['right'].set_color('red')  # Set the color of the twin axis
    ax_spec.yaxis.label.set_color('red')  # Set the color of the twin axis label
    ax_spec.tick_params(axis='y', colors='red')  # Set the color of the twin axis ticks
    ax_spec.set_title('{}'.format(title))

   


# Add colorbar for spectrograms
cbar = fig.colorbar(pcm, ax=axes.ravel().tolist(), pad=0.1)
cbar.set_label('Power Spectral Density (dB/Hz)', rotation=270, labelpad=20)


plt.show()
