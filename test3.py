import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7])
Y = np.array([1.1,1.9,3.0,4.1,5.2,5.8,7])

# plt.scatter (X,Y)
slope, intercept = np.polyfit(X, Y, 1)
plt.plot(X, X*slope + intercept, 'r')

plt.show()