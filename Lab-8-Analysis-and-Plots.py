"""
Author: Brandon Curl
Contact: brandoncurl@utexas.edu
Date: 11/01/2020
"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

#Function to calculate correlation from the observed and theoretical values
def correlation(observed, theoretical):
    r2 = r2_score(observed, theoretical)
    return r2

#Data
v_naught = 100 #Initial Voltage
angle_deg = [100, 100, 100] # List of all angle values in DEGREES
angle_error_deg = [100] * len(angle_deg) # Angle Error in DEGREES
angle = np.radians(angle_deg)
angle_error = np.radians(angle_error_deg)
voltage = [100, 100, 100] # List of all voltage values
voltage_error = [100] * len(voltage) # Voltage Error

#Calculates relevant statistical characteristics
correlation_f = correlation(voltage, v_naught*np.power(np.cos(np.asarray(angle)),2))

#Prints relevant statistical characteristics
print("The correlation of determination of this fit was r^2={}".format(correlation_f))

#Creates the plot
t = np.arange(0, 1.59, 0.02)
plt.plot(angle, voltage, 'bo')
plt.plot(t, v_naught*np.power(np.cos(t), 2), 'r')
plt.errorbar(angle, voltage, yerr = voltage_error, xerr = angle_error, fmt = 'o')
plt.xlabel('Angle (rad)')
plt.xticks([0, 0.393, 0.785, 1.178, 1.571], ['0', r'$\pi/8$', r'$\pi/4$', r'$3\pi/8$', r'$\pi/2$'])
plt.axis([-0.02, 1.6, -0.02, 1.1])
plt.text(1.0, 0.8, r'$V = V_{o} cos^{2}(\theta)$')
plt.text(1.0, 0.75, r'$r^{2} = %s$' % round(correlation_f, 4))
plt.ylabel('Voltage (V)')
plt.title('Malus\'s Law')
plt.show()
