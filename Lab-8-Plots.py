import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

#Function to calculate correlation from the covariance matrix of the fit
def correlation(observed, theoretical):
    r2 = r2_score(observed, theoretical)
    return r2

#Defines the fuction of fringe distance versus adjacent ray distance
def func(d, a, exp):
    return a*np.power(d, exp)

#Data for the experiment
d = [0]
chi = [0]

#Calculates fit parameters and relevant statistical characteristics
popt, pcov = curve_fit(func, d, chi)
a = popt[0]
exp = popt[1]
std_error = np.sqrt(np.diag(pcov)) / len(d) ** (1/2)
correlation = correlation(chi, func(d, a, exp))

#Prints fit parameters and relevant statistical characteristics
print("The power of the fit was {} +/- {} ".format(exp, std_error[1]))
print("The correlation of determination of this fit was r^2={}".format(correlation))
print(a)

#Creates the plot
t = np.arange(0, 1.5, 0.01)
plt.plot(t, func(t, *popt), 'r--')
plt.plot(d, chi, 'bo')
plt.errorbar(d, chi, yerr = [0.05] * len(chi), fmt = 'o') #0.05 was my error
plt.text(1.1, 0.5, r'$\chi = \alpha\lambda^{%s}$' % round(exp, 3))
plt.text(1.1, 0.4, r'$r^{2} = %s$' % round(correlation, 4))
plt.xlabel('Axis Title Here (mm)')
plt.axis([0, 1.5, 0, 0.8])
plt.ylabel('Fringe Distance (cm)')
plt.title('Two-Slit Diffraction')
plt.show()
