from scipy import misc
def f(x):
    return 4*x**2+1
a=misc.derivative(f,7)
print(a)