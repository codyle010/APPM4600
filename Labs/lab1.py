import numpy as np #import numpy
import matplotlib.pyplot as plt

x = np.linspace(0,1,100) #define x using linspace
y = np.arange(0,1,100) #define y using arange

first3 = x[0:3] #defines this variable as the first 3 terms of x
print("the first three entries of x are ", first3) #prints

w = 10**(-np.linspace(1,10,10))
x = np.arange(len(w)) + 1

plt.plot(x,w)
s = 3*w
plt.plot(x,s)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
