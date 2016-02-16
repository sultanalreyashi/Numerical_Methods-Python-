import math
def f(x):
    return x-math.exp(-x)-2

a=2
b=3

for i in range(10):
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    print(i+1,c)
    if f(a)*f(c)>0:
        a=c
    else:
        b=c
print('Done')
   
