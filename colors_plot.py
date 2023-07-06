import numpy as np
import matplotlib.pyplot as plt

def plot_colors():

    # Define the frequency range for visible light (in THz)
    frequency_range = np.linspace(430, 750, num=1000)

    #add correction to make things more visiable 
    cor = 10 

    # Calculate the power (in dB) for each color based on its frequency
    red_power = 10 * np.log10(frequency_range / 430) + cor
    orange_power = 10 * np.log10(frequency_range / 470) + cor
    yellow_power = 10 * np.log10(frequency_range / 510) + cor
    green_power = 10 * np.log10(frequency_range / 565) + cor
    blue_power = 10 * np.log10(frequency_range / 610) + cor
    indigo_power = 10 * np.log10(frequency_range / 670) + cor
    violet_power = 10 * np.log10(frequency_range / 750) + cor

    plt.style.use('dark_background')

    ##plt.gca().set_facecolor('black')

    # Plot the colors of the rainbow
    plt.plot(frequency_range, red_power, color='red', label='Red')
    plt.plot(frequency_range, orange_power, color='orange', label='Orange')
    plt.plot(frequency_range, yellow_power, color='yellow', label='Yellow')
    plt.plot(frequency_range, green_power, color='green', label='Green')
    plt.plot(frequency_range, blue_power, color='blue', label='Blue')
    plt.plot(frequency_range, indigo_power, color='indigo', label='Indigo')
    plt.plot(frequency_range, violet_power, color='violet', label='Violet')

   

    plt.xlabel('Frequency (THz)')
    plt.ylabel('Power (dB)')
    plt.title('Colors of the Rainbow')
    plt.legend()
    ##plt.grid(True)
    #plt.show()

#plot_colors()