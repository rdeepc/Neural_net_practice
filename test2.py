import numpy as np

x=np.array([2104,1600,2400])
y=([399,329,369])

m=[]
m.append(y[0]/x[0])
m.append(y[1]/x[1])
m.append(y[2]/x[2])

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)

print(np.mean(m))
print(fit)