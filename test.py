import numpy as np
import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [3,5,7,10] # 10, not 9, so the fit isn't perfect

x=[2104,1600,2400]
y=[399,329,369]

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)
print(fit)
print(fit_fn)
# # fit_fn is now a function which takes in x and returns an estimate for y
#
plt.plot(fit_fn(x), '-k')
plt.xlim(0, 2500)
plt.ylim(0, 400)
plt.show()