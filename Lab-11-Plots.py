"""
Author: Brandon Curl
Contact: brandoncurl@utexas.edu
Date: 12/08/2020
"""

import matplotlib.pyplot as plt
import numpy as np

# Defines the s and p reflection functions
def s(ia):
    return np.absolute(np.divide(np.cos(ia)-np.power(n**2-np.power(np.sin(ia), 2), .5), np.cos(ia)+np.power(n**2-np.power(np.sin(ia), 2), .5)))

def p(ia):
    return np.absolute(np.divide(np.power(1-np.power(np.sin(ia)/n, 2), .5)-n*np.cos(ia), np.power(1-np.power(np.sin(ia)/n, 2), .5)+n*np.cos(ia)))

# Data points for plotting
n = 0 # Refractive Index from Lab 6
s_reflection = [0]
s_reflection_error = [0]
s_angles = [0]
p_reflection = [0]
p_reflection_error = [0]
p_angles = [0]

# Plots the functions
t = np.arange(0, 1.571, 0.01)
plt.plot(t, s(t), 'r--', label = "S-Polarized")
plt.plot(t, p(t), 'b--', label = "P-Polarized")
plt.plot(value, 0, 'ko', label = 'Brewster\'s Angle') # Enter your Brewster's Angle for 'value'
plt.errorbar(s_angles, s_reflection, xerr = [0.035] * len(p_angles), yerr = s_reflection_error, fmt = 'ro') # I called my angle error 2 deg.
plt.errorbar(p_angles, p_reflection, xerr = [0.035] * len(s_angles), yerr = p_reflection_error, fmt = 'bo') # I called my angle error 2 deg.
plt.xlabel('Angle (rad)')
plt.xticks([0, 0.393, 0.785, 1.178, 1.571], ['0', r'$\pi/8$', r'$\pi/4$', r'$3\pi/8$', r'$\pi/2$'])
plt.axis([0, 1.571, 0, 1])
plt.ylabel('Reflection Coefficient')
plt.title('Reflection Coefficients')
plt.legend()
plt.show()
