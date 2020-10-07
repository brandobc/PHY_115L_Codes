"""
Author: Brandon Curl
Contact: brandoncurl@utexas.edu
Date: 10/5/2020

Anywhere you see 0.762 or 0.0395, these must get changed to your pipe length and pipe diameter, respectively.
Of course, change the 4 lists of data to your data as well as the value of d at the top.
You may additionally need to alter the plot error bars, texts, ticks, and axes.
I used a non-standard library called sklearn.metrics for the coefficient of determination. If you do not have this library and do not want to download it, you can comment out the all of the lines discussing correlation.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

#Sets the diameter of the pipe for end correction
d = 0.0395

#Function to calculate correlation from the covariance matrix of the fit
def correlation(observed, theoretical):
    r2 = r2_score(observed, theoretical)
    return r2

#Defines the fuction of velocity versus mode for an open-open pipe
def func_open(n_open, v_open):
    return np.asarray(n_open) * v_open / (2 * (0.762 + 2 * 0.3 * d))

#Data for the open-open experiment
modes_open = [1, 2, 3, 4, 5]
frequencies_open = [206, 420, 637, 852, 1054]

#Calculates fit parameters and relevant statistical characteristics
popt_open, pcov_open = curve_fit(func_open, modes_open, frequencies_open, bounds = [0, [400]])
velocity_open = popt_open[0]
std_error_open = np.sqrt(np.diag(pcov_open)) / len(modes_open) ** (1/2)
correlation_open = correlation(frequencies_open, func_open(modes_open, velocity_open))

#Prints fit parameters and relevant statistical characteristics
print("The velocity of the open-open pipe was {} m/s +/- {} m/s".format(velocity_open, std_error_open[0]))
print("The correlation of determination of this fit was r^2={}".format(correlation_open))

#Creates the plot for the open-open pipe
plt.plot(modes_open, func_open(modes_open, *popt_open), 'r-')
plt.plot(modes_open, frequencies_open, 'bo')
plt.errorbar(modes_open, frequencies_open, yerr = [5, 5, 5, 5, 5], fmt = 'o') #Not visible
plt.text(1, 1000, r'$f = \frac{(%s m/s)n}{2(0.762 m + 2 * 0.3(0.0395 m))}$' % round(velocity_open, 2))
plt.xlabel('Mode Number')
plt.xticks(np.arange(7), ['0', '1', '2', '3', '4', '5'])
plt.axis([0.5, 5.5, 150, 1100])
plt.ylabel('Frequency (Hz)')
plt.title('Open-Open Pipe')
plt.show()


#Defines the fuction of velocity versus mode for an open-open pipe
def func_closed(n_closed, v_closed):
    return (2 * np.asarray(n_closed) - 1) * v_closed / (4 * (0.762 + 0.3 * d))

#Data for the open-open experiment
modes_closed = [1, 2, 3, 4, 5, 6]
frequencies_closed = [105, 314, 523, 727, 938, 1140]

#Calculates fit parameters and relevant statistical characteristics
popt_closed, pcov_closed = curve_fit(func_closed, modes_closed, frequencies_closed, bounds = [0, [400]])
velocity_closed = popt_closed[0]
std_error_closed = np.sqrt(np.diag(pcov_closed)) / len(modes_closed) ** (1/2)
correlation_closed = correlation(frequencies_closed, func_closed(modes_closed, velocity_closed))

#Prints fit parameters and relevant statistical characteristics
print("The velocity of the closed-closed pipe was {} m/s +/- {} m/s".format(velocity_closed, std_error_closed[0]))
print("The correlation of determination of this fit was r^2={}".format(correlation_closed))

#Creates the plot for the closed-closed pipe
plt.plot(modes_closed, func_closed(modes_closed, *popt_closed), 'r-')
plt.plot(modes_closed, frequencies_closed, 'bo')
plt.errorbar(modes_closed, frequencies_closed, yerr = [5, 5, 5, 5, 5, 5], fmt = 'o') #Not visible
plt.text(1, 1000, r'f = $\frac{(%s m/s)(2n - 1)}{4(0.762 m + 0.3(0.0395 m))}$' % round(velocity_closed, 2))
plt.xlabel('Mode Number')
plt.ylabel('Frequency (Hz)')
plt.title('Open-Closed Pipe')
plt.show()
