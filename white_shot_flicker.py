import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import random
from colors_plot import plot_colors
# Generate random 6-digit hex value

def generate_random_color():

    _ = []
    # Generate random shade of blue in the range of light blue to dark blue
    blue = random.randint(220, 255)

    # Generate random shade of green in the range of light green to dark green
    green = random.randint(201, 255)

    # Generate random shade of red in the range of light red to dark red
    red = random.randint(230, 255)

    # Convert the RGB values to hexadecimal format
    hex_value_blue = '#0000{0:02X}'.format(blue)

    hex_value_green = '#00{0:02X}00'.format(green)

    hex_value_red = '#{0:02X}0000'.format(red)

    _.append(hex_value_red)
    _.append(hex_value_green)
    _.append(hex_value_blue)

    return _


# Generate a list of random colors
random_colors_list = generate_random_color()

# Parameters
duration = 5.0  # Duration of the generated noise in seconds
fs = 1e5/duration  # Sampling frequency in Hz

# Generate white noise 
samples = int(duration * fs)
noise = np.random.randn(samples)


# Compute power spectral density (PSD)
frequencies, psd = signal.welch(noise, fs, nperseg=1024)

# Generate shot noise
shot_noise = np.random.poisson(1.0, int(duration * fs)) - 1.0

# Generate flicker noise
flicker_noise = np.cumsum(np.random.randn(int(duration * fs)))

# Compute power spectral density (PSD)
frequencies, shot_psd = signal.welch(shot_noise, fs, nperseg=1024)
_, flicker_psd = signal.welch(flicker_noise, fs, nperseg=1024)

# Calculate frequency response
_, shot_freq_resp = signal.freqz(shot_noise, 1, fs=fs)
_, flicker_freq_resp = signal.freqz(flicker_noise, 1, fs=fs)
_, noise_freq_resp = signal.freqz(noise, 1, fs=fs)


# Set plot style with black background
plt.style.use('dark_background')

# Plotting
fig = plt.figure(figsize=(22, 15))

# Set the spacing between subplots
fig.subplots_adjust(hspace=0.8, wspace=0.2)


                        ###TIME DOMAIN###


# Plot time-domain waveform
ax1 = fig.add_subplot(3, 3, 1)
time = np.linspace(0, duration, samples)
ax1.plot(time, noise , color=random_colors_list[0])
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.set_title('White Noise - Time Domain')

# Plot shot noise
ax6 = fig.add_subplot(3, 3, 4)
time = np.linspace(0, duration, len(shot_noise))
ax6.plot(time, shot_noise , color=random_colors_list[0])
ax6.set_xlabel('Time (s)')
ax6.set_ylabel('Amplitude')
ax6.set_title('Shot Noise - Time Domain')

# Plot flicker noise
ax9 = fig.add_subplot(3, 3, 7)
time = np.linspace(0, duration, len(flicker_noise))
ax9.plot(time, flicker_noise , color=random_colors_list[0])
ax9.set_xlabel('Time (s)')
ax9.set_ylabel('Amplitude')
ax9.set_title('Flicker Noise - Time Domain')


                        ###FREQ DOMAIN###


# Plot white noise frequency response
ax3 = fig.add_subplot(3, 3, 2)
freq = np.linspace(0, fs / 2, len(noise_freq_resp))
ax3.plot(freq, 20 * np.log10(np.abs(noise_freq_resp)) , color=random_colors_list[1])
ax3.set_xlabel('Frequency (Hz)')
ax3.set_ylabel('Magnitude (dB)')
ax3.set_title('White Noise - Frequency Response')

# Plot shot noise frequency response
ax5 = fig.add_subplot(3, 3, 5)
freq = np.linspace(0, fs / 2, len(shot_freq_resp))
ax5.plot(freq, 20 * np.log10(np.abs(shot_freq_resp)) , color=random_colors_list[1])
ax5.set_xlabel('Frequency (Hz)')
ax5.set_ylabel('Magnitude (dB)')
ax5.set_title('Shot Noise - Frequency Response')

# Plot flicker noise frequency response
ax8 = fig.add_subplot(3, 3, 8)
freq = np.linspace(0, fs / 2, len(flicker_freq_resp))
ax8.plot(freq, 20 * np.log10(np.abs(flicker_freq_resp)) , color=random_colors_list[1])
ax8.set_xlabel('Frequency (Hz)')
ax8.set_ylabel('Magnitude (dB)')
ax8.set_title('Flicker Noise - Frequency Response')


                        ###PSD DOMAIN###


# Plot power spectral density (PSD)
ax3 = fig.add_subplot(3, 3, 3)
ax3.semilogx(frequencies, 10 * np.log10(psd) , color=random_colors_list[2])
ax3.set_xlabel('Frequency (Hz)')
ax3.set_ylabel('Power Spectral Density (dB/Hz)')
ax3.set_title('White Noise - Power Spectral Density')

# Plot shot noise PSD
ax6 = fig.add_subplot(3, 3, 6)
ax6.semilogx(frequencies, 10 * np.log10(shot_psd) , color=random_colors_list[2])
ax6.set_xlabel('Frequency (Hz)')
ax6.set_ylabel('Power Spectral Density (dB/Hz)')
ax6.set_title('Shot Noise - Power Spectral Density')

# Plot flicker noise PSD
ax9 = fig.add_subplot(3, 3, 9)
ax9.semilogx(frequencies, 10 * np.log10(flicker_psd) , color=random_colors_list[2])
ax9.set_xlabel('Frequency (Hz)')
ax9.set_ylabel('Power Spectral Density (dB/Hz)')
ax9.set_title('Flicker Noise - Power Spectral Density')

##plt.show()

# Plotting
fig = plt.figure(figsize=(22, 81))

# Set the spacing between subplots
fig.subplots_adjust(hspace=0.4)

fig.subplots_adjust(hspace=0.4)

# Plot colors of the rainbow associated with each noise
ax1 = fig.add_subplot(2, 1, 1)

plot_colors()

# Plot power spectral density (PSD) of each noise
ax2 = fig.add_subplot(2, 1, 2)
ax2.semilogx(frequencies, 10 * np.log10(psd), color='white', label='White Noise')
ax2.semilogx(frequencies, 10 * np.log10(shot_psd), color='blue', label='Shot Noise')
ax2.semilogx(frequencies, 10 * np.log10(flicker_psd), color='red', label='Flicker Noise')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Power Spectral Density (dB/Hz)')
ax2.set_title('Power Spectral Density of Different Noises')
ax2.legend()

plt.show()