#!/usr/bin/env python
# coding: utf-8

# [Back to Assignment 3](_Oving3.ipynb)
# 
# # Newton's method
# In this exercise you will use Newton's method for finding roots of the scalar function $f(x)$ to within a certain level of prescision (i.e., some small number $\texttt{tol}$). Recall that with Newton's method, you make a guess for the root $x_0$, and then you draw a tangent line of $f(x)$ line at $x=x_0$. You then use the root of the tangent line as an $\it{improved}$ guess of the root, which we will call $x_1$. We then draw another tangent line, now at the point $x_1$ and keep going $n$ times until your guess $x_{n}$ satifies some sort of stopping criteria. 
# 
# Newton's method reads $$x_{k+1}=x_{k}-\frac{f(x_{k})}{f'(x_{k})},$$ which is the solution to the root of the tangent line of $f(x)$ at $x=x_k$. Note that this is best implemented using a while loop. 
# 
# **Stopping criteria**: Your stopping criteria should be something like $\texttt{abs}(f(x_n))<\texttt{tol}$ and/or $\texttt{abs}(x_n-x_{n+1})<\texttt{tol}$. In addition, it is sometimes wise to add another stopping criteria in case the algorithm $\it does~not$ converge, for example 
# 
#     k=1
#     while <<stopping_criteria>> and k<100:
#         <<Newton iteration>>
#         k = k+1
#         
# this will stop the loop if it hasn't converged in 100 iterations.
# 
# 

# ## a) 

# Use Newton's method to calculate the roots of the test function $f(x)=\cos(x)$, which has known roots at $x = \frac{n \pi}{2}$, for some integer $m$. 
# 
# Use a tolerance of $\texttt{tol} = 10^{-10}$, and an initial guess of $x_0 = 0.5$.
# 
# Your algorithm should converge to the root $x = \frac{\pi}{2}$. 

# In[11]:


# write your code here
from math import cos
from math import sin
from math import pi
x = 0
x_old = 0.5 
tol = 1e-10 
k = 1

while (abs(cos(x_old)) >= tol) and (k < 100):
    print(x)
    print(x_old)
    x = x_old - (cos(x_old)/(-sin(x_old)))
    x_old = x
    print(k)
    k += 1
print("The answer converges to : ", x_old, " with k = ", k-1)
print("The root is : ", pi / 2)


# ### i) ###
# For the stopping criteria $\texttt{abs}(f(x_n))<\texttt{tol}$, how many iterations does it take for Newton's method to converge to the root? 
# 
# 

# **Answer:** 5

# ### ii) ### 
# What happens when you use the initial guess of $x_0 = 0$? Can you explain your observation? (Note: if you have written your code correctly, something $\it should$ go wrong.)

# In[12]:


# write your code here
from math import cos
from math import sin
from math import pi
x = 0
x_old = 0 
tol = 1e-10 
k = 1

while (abs(cos(x_old)) >= tol) and (k < 100):
    print(x)
    print(x_old)
    x = x_old - (cos(x_old)/(-sin(x_old)))
    x_old = x
    print(k)
    k += 1
print("The answer converges to : ", x_old, " with k = ", k-1)
print("The root is : ", pi / 2)


# **Answer:** Iteration does not go further because f'(x_n) is zero (-sin(0) = 0).

# ### iii)

# What happens when you use a tolerance of $\texttt{tol} = 10^{-18}$ and $x_0=0.5$? Does the algorithm converge? Can you explain your observation?

# In[ ]:


# write your code here
from math import cos
from math import sin
from math import pi
x = 0
x_old = 0.5 
tol = 1e-14
k = 1

while (abs(cos(x_old)) >= tol): #and (k < 100):
    #print(x)
    #print(x_old)
    x = x_old - (cos(x_old)/(-sin(x_old)))
    x_old = x
    print(k)
    k += 1
print("The answer converges to : ", x_old, " with k = ", k-1)
print("The root is : ", pi / 2)


# **Answer:** No. Iteration does not stop after k > 61266 .... so on. This is because the truncation error from python is more than 1e-18.

# ## b)

# Now we will try and find a solution to the following function $$x{{\rm e}^{- \left( \sin \left( x/2 \right)  \right) ^{2}}}=3/2. $$ To do this we will look for a root of the function $$ f(x) = x{{\rm e}^{- \left( \sin \left( x/2 \right)  \right) ^{2}}}-3/2.$$
# which has the derivative $$f'(x) = {{\rm e}^{- \left( \sin \left( x/2 \right)  \right) ^{2}}}-x\sin
#  \left( x/2 \right) \cos \left( x/2 \right) {{\rm e}^{- \left( \sin
#  \left( x/2 \right)  \right) ^{2}}}.
# $$ The values of $f(x)$ and $f'(x)$ for $x = 2$ have been written in Python for you below so you don't make a mistake copying the formula into you code. 

# In[39]:


import math 
x = 2
f = x*math.exp(-math.sin((1/2)*x)**2)-3/2
dfdx = math.exp(-math.sin((1/2)*x)**2)-x*math.sin((1/2)*x)*math.cos((1/2)*x)*math.exp(-math.sin((1/2)*x)**2)
print("The value of the derivative at x = 2 is f'(2) =", dfdx)


# Notice that the value for the derivative at $x=2$ is very close to zero and is therefore not a good starting point. 

# ### i) ### 
#  There is a root in the interval $[0,10]$. What is the value of this root? Express your answer to 10 decimal places.  
# 
# **Note:** As suggested above, the Newton method might not converge for certain initial values, therefore you need to test a few initial starting points until the algorithm converges. 
# 

# In[27]:


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
    x = x_new
    k += 1
    
    f = x*math.exp(-math.sin((1/2)*x)**2)-3/2
    dfdx = math.exp(-math.sin((1/2)*x)**2)-x*math.sin((1/2)*x)*math.cos((1/2)*x)*math.exp(-math.sin((1/2)*x)**2)
    
    x_new = x - (f / dfdx) 
    print("x_new = ", x_new)
    print(abs(x_new - x))
    print(tol)
    print(abs(x_new - x) > tol)
    
    
print("The answer converges to : ", x, " with k = ", k)
print("n = %-2d: x_n = %.10f, f(x_n) = %.5e" % (k, x, f)) 


# #### **Hint:**

# 
# The below code can be used to print values to many decimal places. To get 10 decimal places of accuracy, you should keep iterating your code until the first 10 decimal places of ${x_n}$ don't change between iterations

# In[36]:


n = 1
x = 1/7
f = x*math.exp(-math.sin((1/2)*x)**2)-3/2

print("n = %-2d: x_n = %.10f, f(x_n) = %.5e" % (n,x,f)) 
# this prints the integer n, the float x to 10 decimal places
# ... and the float f to 5 decimal places (in exponential format). This 
# ... is best placed inside your loop to see what is happening at each iteration 


# ### ii) (Optional bonus question for an extra reward*!) ###

# As you may have noticed, Newton's method sometimes doesn't converge unless we are close enough to the solution. One very common method to cirmumvent this issue is to do a few bisection method iterations first, and when you are "close enough" to the solution you can bring it home with Newton iterations. 
# 
# Implement a root finding algorithm that:
# 
#    (1) uses the bisection method until you are within $|f(c)|<\texttt{tol1}$, then
#     
#    (2) uses Newton's method until  $|f(x_n)|<\texttt{tol2}$, 
#     
# where you can choose the values of $\texttt{tol1}$ and $\texttt{tol2}$ as long as $\texttt{tol1}>\texttt{tol2}$.

#  \* The reward is the satisfaction of completing the hardest part of the assignment (+ read the assignment approval description for assignment 3)

# In[ ]:


# write your for b-ii) here




