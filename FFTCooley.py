'''
program : FFTCooley.py
author: Prashanth
course:CS 827
date: 2018/10/29
assignment # 3
description :this program is the implementation of Cooley Tukey algorithm.
             This program will take amplitudes as input and generates original 
             signal and Real TTF value figures as output.
                         
'''
#importing numpy module
import numpy as np
#importing matplotlib to plot figures
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq,ifft

#number of sample points
n = 1000

#Distance in meters or time period (in sedonds), periodicity
Lx = 100

#taking amplitudes as input
a1 = float(input('Enter amplitude in decimal'))
a2 = float(input('Enter second  amplitude in decimal'))
a3 = float(input('Enter  third amplitude in decimal'))

#angular frquency
omg = 2.0*np.pi/Lx

##Creating ind signals
x = np.linspace(0,Lx,n)
y1 = a1*np.cos(5.0*omg*x)
y2 = a2*np.cos(10.0*omg*x)
y3 = a3*np.cos(20.0*omg*x)

#Full Signal
y = y1 + y2 + y3

#Creating necessary frequencies
freq = fftfreq(n)


#mask array is used for power spectra. It is used to avoid negative requencies
#ignoring half the values as they are complex conjuates of other
mask = freq>0

#FFT and power spectra calucaltions
#fft values
fft_vals = fft(y)

#true theoretical fft
fft_theo = 2.0*np.abs(fft_vals/n)

#plotting original square by taking x and y
plt.figure(1)
plt.title('Original Signal')
plt.plot(x,y,color='xkcd:salmon',label='original')
plt.legend()

#plotting real fft values by takibg fft_vals and fft_theo
plt.figure(2)
#plt.plot(freqs,fft_vals, label= raw fft values)
plt.plot(freq[mask], fft_theo[mask], label="true fft values")
plt.title("True FFT values")
plt.show()




