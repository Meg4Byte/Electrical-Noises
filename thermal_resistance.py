import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Set parameters
Rmin = 1000  # minimum resistance in ohms
Rmax = 115000  # maximum resistance in ohms
B = 2e6  # bandwidth in Hz
N = int(B/2)  # number of samples
T = 300  # temperature in K
Fs = B  # sampling frequency

# Calculate RMS voltage of thermal noise for fixed temperature
k = 1.38e-23  # Boltzmann constant in J/K
Vrms = np.sqrt(4 * k * Rmin * B * (T/300))

# Initialize lists
Rs = np.arange(Rmin, Rmax, 15000)
PSDs = []

# Generate thermal noise and calculate PSD for each resistance
for R in Rs:

    # Calculate factor to adjust RMS voltage for temperature
    factor = np.sqrt(T/300)

    # Generate thermal noise with adjusted RMS voltage
    Vrms = np.sqrt(4 * k * R * B * (T/300))
    noise = np.random.normal(scale=Vrms*factor, size=N)

    # Calculate PSD using Welch's method
    f, Pxx_den = signal.welch(noise, Fs, nperseg=1024, scaling='density')
    PSDs.append(10 * np.log10(Pxx_den))

# Set plot style
plt.style.use('dark_background')

# Plot all PSDs on same graph
fig, ax = plt.subplots()
ax.set_xscale('log')

# ax.set_yscale('log') - No need to log-scale the y-axis when using dB scale
for i, R in enumerate(Rs):
    # Convert PSDs to dB
    PSD_dB = PSDs[i]
    ax.plot(f, PSD_dB, label='R = {} k{}'.format(R/1000 , chr(937)))

ax.legend()
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('PSD [dB/Hz]')
ax.set_title('Thermal Noise PSD for Different Resistance Values')
plt.show()
