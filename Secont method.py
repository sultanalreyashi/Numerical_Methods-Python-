import math
def f(x):
    return math.tan(x)-1.2

a=.5
b=1

for i in range(2):
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    print(i+1,c)
    a=b
    b=c
    
print('Done')
   
