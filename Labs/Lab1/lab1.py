import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = np.arange(0,1,100)

first3 = x[0:3]
print("the first three entries of x are ", first3)

w = 10**(-np.linspace(1,10,10))
x = np.arange(len(w)) + 1

plt.plot(x,w)
s = 3*w
plt.plot(x,s)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
