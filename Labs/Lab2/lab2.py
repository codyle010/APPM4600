import numpy as np

# define routines
def fixedpt(f,x0,tol,Nmax):
    count = 0
    while (count <Nmax):
        count = count +1
        x1 = f(x0)
        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar,ier, count]
        x0 = x1
    xstar = x1
    ier = 1
    return [xstar, ier, count]

def convergence_order(p,p_hat):
    return np.log(abs((p_hat[-1]-p)/(p_hat[-2]-p)))/np.log(abs((p_hat[-2]-p)/(p_hat[-3]-p)))
        
g1 = lambda x: (10/(x+4)) ** 0.5


[xstar,ier, count] = fixedpt(g1,1.5,10e-10,100)
print('the approximate fixed point is:',xstar)
print('g1(xstar):',g1(xstar))
print('Error message reads:',ier)
print('found at iteration ',count)
