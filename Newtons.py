import math
def f(x):
    return math.exp(x)-50*x
a=6
def g(x):
    return math.exp(x)-50
def h(x):
    return a-(f(x)/g(x))
for i in range(50):
    a=h(a)
    print(i+1,a)
print("Done!")
