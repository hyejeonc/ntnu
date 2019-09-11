#!/usr/bin/env python
# coding: utf-8

# # Tetrahedron
# 
# **Learning goals:**
# 
# * Input/output
# * Formatting printed text
# * Using built-in functions
# 
# **Starting Out with Python:**
# 
# * ch. 2.8
# 
# ![img](./../Resources/Images/Tetrahedron.jpg)
# 
# <br><br>In this task you will find the surface area and volume of regular tetrahedrons (also known as triangular pyramids). A regular tetrahedron is a geometrical object consisting of four equilateral triangles.
# 
# * **The surface area of a tetrahedron is $A=\sqrt{3}a^{2}$**  
# * **The volume of a tetrahedron is $V=\frac{\sqrt{2}a^{3}}{12}$  Where $a=\frac{3}{\sqrt{6}}h$** 

# ## a)

#  Create a program which compute and prints the surface area of a tetrahedron. Verify that the program prints 23.383 when they height is 3 (it doesnt matter if the answer has more digits than this).
#  
#  
# **Example run** 
# ```python
# A tetrahedron with height 3 has area 23.383
# ```
# 
# ***Write the code in the block below.***

# In[5]:


import math
h = 3
a = 3 * h / math.sqrt(6)
area =  math.sqrt(3) * a**2
area
print('A tetraheron with height ', h, ' has area ', area)


# #### Hint

# Square roots can be computed either by raising the number to the power of 1/2, for example `x ** 0.5`, or by using import `math` and `math.sqrt` to compute the square roots.

# ## b)

# Expand the program such that it also prints the volume of a tetrahedron. Verify that the program prints 5.846 when the height is 3 (it doesn't matter if the answer has more digits than this).
# 
# **Example run:**
# 
# ```python
# A tetrahedron with height 3 has volume 5.846
# ```
# 
# Write the code in the block below.

# In[6]:


vol = math.sqrt(2) * a**3 / 12
print('A tetraheron with height ', h, ' has volume ', vol)


# ## c)

# Expand the program so that the user is asked to provide the value for the height which is used to compute and output the volume and area
# 
# **Example run:**
# 
#   
# ```python
# Enter a height: 3
#     
# A tetrahetron with height 3.0 has volume 5.85 and area 23.38.
# ```
# 
# Write the code in the block below.

# In[10]:


h = float(input('Enter a height: '))
a = 3 * h / math.sqrt(6)
vol = math.sqrt(2) * a**3 / 12
area =  math.sqrt(3) * a**2
print('A tetraheron with height ', h, ' has volume ', vol, ' and area ', area)


# In[ ]:




