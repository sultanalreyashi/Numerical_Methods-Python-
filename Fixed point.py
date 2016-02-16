import math
import cmath

def f(x):
    return x**3+x**2-100
a=0
def g(x):
    return 100/(x**2+x)
for i in range(10):
    a=g(a)
    print(i+1,a)
print ("Done")
