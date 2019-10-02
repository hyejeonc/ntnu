# Write your code here
import math
x = 5

tol = 1e-10
k = 0

f = x*math.exp(-math.sin((1/2)*x)**2)-3/2
dfdx = math.exp(-math.sin((1/2)*x)**2)-x*math.sin((1/2)*x)*math.cos((1/2)*x)*math.exp(-math.sin((1/2)*x)**2)
x_new = x - (f / dfdx)

print("The value of the derivative at x = ", x,"is f'(5) =", dfdx)

while (abs(x_new - x) > tol) and (k < 100):
    print("k = ", k)
    print("x = ", x)
    
    k += 1
    
    f = x*math.exp(-math.sin((1/2)*x)**2)-3/2
    dfdx = math.exp(-math.sin((1/2)*x)**2)-x*math.sin((1/2)*x)*math.cos((1/2)*x)*math.exp(-math.sin((1/2)*x)**2)
    
    x_new = x - (f / dfdx) 
    print("x_new = ", x_new)
    print(abs(x_new - x))
    print(tol)
    print(abs(x_new - x) > tol)
    x = x_new
    
    
    
print("The answer converges to : ", x, " with k = ", k)
print("n = %-2d: x_n = %.10f, f(x_n) = %.5e" % (k, x, f)) 

