import math
def f(x):
    return x**3+x**2-100 #place function here
#intialize the values
a=-1
b=1
i=1
while b-a>.0000001:
    c=(a+b)/2
    print(i,c)
    i+=1
    if f(a)*f(c)>0:
        a=c
    else:
        b=c
print("We're done")
