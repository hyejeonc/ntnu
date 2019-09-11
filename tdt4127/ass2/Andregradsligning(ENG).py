#!/usr/bin/env python
# coding: utf-8

# # Second Degree Equations
# 
# **Learning goals:**
# - Conditions
# 
# **Starting Out with Python:**
# - Ch. 3.4

# In this assignment, you will create a program that takes input from the user about the numbers in a second-degree equation, and returns whether the equation has two real solutions, two imaginary solutions or one real double root. In addition, the program should return the solutions if they are real.
# 
# The general form of a second-degree equation is
# 
# \begin{equation*}
# ax^2 + bx + c = 0
# \end{equation*}
# 
# To find out how many solutions and what solution area a second degree equation has, you can use the *discriminant*
# 
# \begin{equation*}
# d = b^2 - 4ac
# \end{equation*}
# 
# And the table
# 
# Case|Solution Area|Amount of roots
# ---|---|---
# d < 0|Imaginary|2
# d > 0|Real|2
# d = 0|Real	1|(double root)

# ## a) Find the correct type of solution

# ***Create a program that asks for the three values a, b and c, calculates d, and tells the user whether the equation has two imaginary solutions, two real solutions, or one real double root.***
# 
# Check for all three possible outcoumes:
# 
# - Two imaginary solutions
#   - example : a = 2, b = 4, c = 9
# - Two real solutions
#   - example : a = 2, b = -5, c = 0
# - One real double root
#   - example: a = 2, b = 4, c = 2
#   
# ***Write code below***

# In[3]:


a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = b**2 - 4*a*c
if d < 0 :
    print('The second degree equation ', a, '*x^2 + ', b, '*x + ', c, 'has two imaginary solutions')
elif d > 0:
    print('The second degree equation ', a, '*x^2 + ', b, '*x + ', c, 'has two real solutions')
else:
    print('The second degree equation ', a, '*x^2 + ', b, '*x + ', c, 'has a real double root')    


# ## b) Real solutions

# ***Expand the program from a) such that the user can get the solution(s) if it(they) is(are) real. ***
# 
# The second degree formula to find the solution(s):
# 
# \begin{equation*}
# x=\frac{-b±\sqrt{d}}{2a}
# \end{equation*}
# 
# **Example run:**
# 
# ```python
# #Example 1: imaginary solutions  
# a: 2  
# b: 4  
# c: 9  
# The second degree equation 2.00*x^2 + 4.00*x + 9.00 has two imaginary solutions
# ```
# 
# ```python
# #Example 2: real løsninger
# a: 2
# b: -5
# c: 0
# The second degree equation 2.00*x^2 -5.00*x + 0.00 has the two real solutions 2.50 and 0.00
# ```
# 
# ```python
# #Example 3: real double root
# a: 2
# b: 4
# c: 2
# The second degree equation 2.00*x^2 + 4.00*x + 2.00 has a real double root -1.00
# ```
# 
# **Write code below**

# In[7]:


import math
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = b**2 - 4*a*c
if d < 0 :
    print('The second degree equation ', a, '*x^2 + ', b, '*x + ', c, 'has two imaginary solutions')
elif d > 0:
    val1 = (-b + math.sqrt(d)) / (2*a)
    val2 = (-b - math.sqrt(d)) / (2*a)
    print('The second degree equation ', a, '*x^2 + ', b, '*x + ', c, 'has two real solutions ', val1, 'and', val2)
else:
    val = (-b) / (2*a)
    print('The second degree equation ', a, '*x^2 + ', b, '*x + ', c, 'has a real double root', val)    


# ## C) (voluntary) Loss of significance

# The second degree formula can in some cases give the wrong answer. One such case is when using it on the equation  $x^2+9^{12}x−3=0$ . If you want to find the roots of this equation, the standard formula gives the following result:
# 
# ```python
# The second degree equation 1.00*x^2 + 282429536481.00*x -3.00 has two real solutions 0.000e+00 and -2.824e+11
# ```
# 
# Here only the last of the roots is correct. The first root has been incorrectly zero due to rounding errord because of a loss of precision in the calculation, correct answer would have been:
# 
# ```python
# The second degree equation 1.00*x^2 + 282429536481.00*x -3.00 has two real solutions 1.062e-11 og -2.824e+11
# ```
# What causes this error? ***Rewrite the program to take such cases into account.***
# 
# **Example**
# ```python
# #a = 0.25, b = 18000, c = 1
# #Old code giving wrong answer:
# The second degree equation  0.25*x^2 + 18000.00*x + 1.00 has two real solution -0.00 and -72000.00
# #Correct answer:
# The second degree equation  0.25*x^2 + 18000.00*x + 1.00 has two real solution -5.556e-05 and -7.200e+04
#   
# #a = 10, b = 25000, c = 0.015
# #Old code giving wrong answer:
# The second degree equation  10.00*x^2 + 25000.00*x + 0.01 has two real solution -0.00 and -2500.00
# #Correct answer:
# The second degree equation  10.00*x^2 + 25000.00*x + 0.01 has two real solution -6.000e-07 and -2.500e+03
# ```

# #### Hint

# If you are having problems, these resources might help you:
# 
# - [NumericallyStableSolutionForTheQuadraticEquations](http://www.solipsys.co.uk/cgi-bin/sews.py?NumericallyStableSolutionForTheQuadraticEquation)
# - [Numerically Stable Method for Solving Quadratic Equations](https://people.csail.mit.edu/bkph/articles/Quadratics.pdf)
