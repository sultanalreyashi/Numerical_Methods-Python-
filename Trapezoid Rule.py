import math

A=float(input("Enter intial point"))
B=float(input("Enter the endpoint"))

def f(x):
    return 2/(x-4)
    #return x**4
    
h=(B-A)
x=A
S=f(A)
x=A+h

while B-x > h/2:
    S=S+2*f(x)
    x=x+h

S=S+f(B)
Integral= (h/2)*S

print()
print('The integral is', Integral)
print('the error should be of the order of', h**3)#for simple
