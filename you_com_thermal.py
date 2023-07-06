import numpy as np
import matplotlib.pyplot as plt

# Set parameters
R = 5000  # resistance in ohms
B = 2000000  # bandwidth in Hz
N = 1000000  # number of samples
temperatures = range(20, 420, 100)  # range of temperatures to sweep

# Calculate RMS voltage of thermal noise for each temperature
k = 1.380649e-23  # Boltzmann constant in J/K
Vrms = np.sqrt(4 * k * R * B)

# Set plot style with black background
plt.style.use('dark_background')

# Generate and plot thermal noise for each temperature
for T in temperatures:

  # Calculate factor to adjust RMS voltage for temperature
  factor = np.sqrt(T/300)

  # Generate thermal noise with adjusted RMS voltage
  noise = np.random.normal(scale=Vrms*factor, size=N)

  # Plot time domain
  plt.subplot(3, len(temperatures), temperatures.index(T) + 1)
  plt.plot(noise, color='blue')
  plt.title('R = {} T = {}K - Time Domain'.format(R , T))
  plt.xlabel('Sample')
  plt.ylabel('Amplitude (V)')

  # Plot frequency domain
  plt.subplot(3, len(temperatures), len(temperatures) + temperatures.index(T) + 1)
  plt.magnitude_spectrum(noise, Fs=B, scale='dB', color='orange')
  plt.title('R = {} T = {}K - Frequency Domain'.format(R , T))
  plt.xscale('log')
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Magnitude (dB)')

  # Calculate and plot PSD using Welch's method
  plt.subplot(3, len(temperatures), 2*len(temperatures) + temperatures.index(T) + 1)
  f, Pxx_den = plt.psd(noise, NFFT=2048, Fs=B, scale_by_freq=True, color='green')
  plt.title('R = {} T = {}K - Power Spectral Density'.format(R , T))
  plt.xscale('log')
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Power/Frequency (dB/Hz)')

# Adjust layout and show plot
plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()
