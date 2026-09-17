import numpy as np
import math

#3.6
f = lambda x: np.exp(x**2 + 7*x -30) + 3
f1 = lambda x: (2*x + 7) * np.exp(x**2 + 7*x -30)
f2 = lambda x: (4*x**2 + 28*x + 51) * np.exp(x**2 + 7*x -30)
tol = 1e-10
a = 2
b = 4

#3.1
"""
Fixed point says that newton will converge if |g'(x*)| < 1
and g(x) = x - f(x) / f'(x)
"""
#3.2,3,4
#3.3 I had to add the first and second derivative of f to find the convergence.
#3.5 This fancy method is faster, but requires more stuff to run. It also has more opportunity to get stuck.
def bisection_to_newtons(f,f_1,f_2,a,b,Nmax,tol):
    fa = f(a)
    fb = f(b);
    p = np.zeros(Nmax+1);
    p[0] = a
    g_pr = lambda x: 1 - (f_1(x)*f_2(x) - f_1(x)**2)/(f_1(x)**2)
    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, ier]
    # verify end points are not a root
    if (fa == 0):
        astar = a
        ier =0
        return [astar, ier]
    if (fb ==0):
        astar = b
        ier = 0
        return [astar, ier]

    d = 0.5*(a+b)
    for it in range(Nmax):
        if (abs(g_pr(d)) >= 1):
            fd = f(d)
            if (fd ==0):
                astar = d
                ier = 0
                return [astar, ier]
            if (fa*fd<0):
                b = d
            else:
                a = d
                fa = fd
            d = 0.5*(a+b)
            # print('abs(d-a) = ', abs(d-a))
        if (abs(g_pr(d)) < 1):
            p1 = p0-f(p0)/fp(p0)
            p[it+1] = p1
            if (abs(p1-p0) < tol):
                pstar = p1
                info = 0
                return [p,pstar,info,it]
            p0 = p1
        pstar = p1
        info = 1
        return [p,pstar,info,it]
    
    astar = d
    ier = 0
    print('count = ', it)
    return [astar, ier]



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

def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    print('count = ', count)
    return [astar, ier]
      
def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]




[astar,ier] = bisection(f,a,b,tol)
print('the approximate root is',astar)
print('the error message reads:',ier)
print('f(astar) =', f(astar))
print('that was bisection')

Nmax = 100

(p,pstar,info,it) = newton(f,f1,3,tol, Nmax)
print('the approximate root is', '%16.16e' % pstar)
print('the error message reads:', '%d' % info)
print('Number of iterations:', '%d' % it)
print('that was newton')

[p,pstar,info,it] = bisection_to_newtons(f,f1,f2,a,b,Nmax,tol)
print('the approximate root is', '%16.16e' % pstar)
print('the error message reads:', '%d' % info)
print('Number of iterations:', '%d' % it)
print('that was both')

        
