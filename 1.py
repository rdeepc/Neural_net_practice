import matplotlib.pyplot as plt
import numpy as np

x=[2104,1600,2400]
y=[399,329,369]

data=[[2104,399],[1600,329],[2400,369]]
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)
plt.plot(x, np.poly1d(np.polyfit(x, y, 1))(x))
plt.plot([data[0][0]],[data[0][1]],'ro')
plt.plot(data[1][0],data[1][1],'ro')
plt.plot(data[2][0],data[2][1],'ro')

plt.plot(fit_fn(y),'--k')

plt.title('House Price')
plt.ylabel('Price Y axis')
plt.xlabel('Area X axis (sq rt)')
plt.xlim(1200,2500)
plt.ylim(200,500)


plt.show()

# print(data)