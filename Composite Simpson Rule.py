import math

A=float(input("Enter intial point"))
B=float(input("Enter the endpoint"))
C=int(input("How many subdivisions?"))

def simpson(f, a, b, n):
    h=(b-a)/n
    S=f(a)

    for i in range(1,n,2):
        x = a+ h*i
        S += 4*f(x)

    for i in range(2,n-1,2):
        x = a+ h*i
        S += 2*f(x)    
        
    S+= f(b)
    F = (h*S)/3

    return F

def f(x): return 1/(x**3+1)
h = abs(B-A)/C

print()
print('The integral is', simpson(f, A, B, C))
print('the error should be of the order of', h**4)#for composite
