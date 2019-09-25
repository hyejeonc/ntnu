#!/usr/bin/env python
# coding: utf-8

# [Back to Assignment 3](_Oving3.ipynb)
# 
# # Fibonacci
# 
# **Learning goals:**
# 
# * Loops
# 
# **Starting Out with Python:**
# 
# * Kap. 4.3
# 
# <br><br>
# In this task you are going to use loops to calculate Fibonacci numbers.
# 
# Fibonacci numbers are defined as follows: 
# 
# * **f(0) = 0**
# * **f(1) = 1**
# * **f(k) = f(k−1) + f(k−2)**
# 
# This means that the two first numbers in the series are 0 and 1. After this, the next number is the sum of the two previous numbers. The beginning of the series looks like this: 0 1 1 2 3 5 8 13 ...

# **a)** Create a program that calculates and returns the k-th fibonacci number f(k) by iterations. If you have done it correctly, the 10th fibonaccinumber f(10) = 55. **Remember that the first number in the sequence is 0**.
# 
# ***Write your code below:***

# In[7]:


import numpy as np

a = np.zeros(100)
a[0] = 0
a[1] = 1

for i in range(2, 100):
    a[i] = int(a[i-1] + a[i-2]) 

    
print(a[10])


# **b)** Rewrite the program in a) such that it also calculates the sum of all fibonacci numbers up to f(k). If you have done this correctly the sum of fibonacci numbers up to the 10th should be 143.

# In[11]:


import numpy as np

a = np.zeros(100)
a[0] = 0
a[1] = 1
sum = np.zeros(100)
sum[0] = 0
sum[1] = 1
for i in range(2, 101):
    a[i] = int(a[i-1] + a[i-2]) 
    sum[i] += sum[i-1] + a[i]
    
print(a[10])
print(sum[10])


# **c)** (**Voluntary**, harder task) Modify the program to return a list of all the fibonacci numbers from 0 to f(k). Print the list. 

# In[3]:


import numpy as np

a = np.zeros(100)
a[0] = 0
a[1] = 1
sum = np.zeros(100)
sum[0] = 0
sum[1] = 1
for i in range(2, 100):
    a[i] = int(a[i-1] + a[i-2]) 
    sum[i] += sum[i-1] + a[i]
    
    
k = 100
for i in range(0, k):
    print(" {:.0f} ".format(a[i]) )
    print(" %.0f " % a[i] )


# In[ ]:




