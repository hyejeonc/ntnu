#!/usr/bin/env python
# coding: utf-8

# 
# # Baking course
# 
# 
# **Learning goals:**
# - Pretty-printing text
# - Performing simple computations
# 
# **Starting Out with Python:**
# 
# - Chapter. 2.3
# - Chapter. 2.8
# - Chapter. 8
# 
# In this assignment you will compute the amount of ingredients required to make cookies and print the result prettily to the screen.
# 
# You are making cookies, and you have a recipe which yields 48 cookies. The recipe requires the following ingredients:
# 
# - 400g sugar 
# - 320g butter
# - 500g chocolate
# - 2 eggs 
# - 460g flour 

# ## a)

# Ask the user about how many cookies they want to make, and output how many ingredients are required to make that amount of cookies
# 
# Example run:
# 
#   
# ```python
# How many cookies do you wish to make? 24
# Number of cookies: 24 
# Sugar (g): 200.0
# Butter (g): 160.0
# Choocolate (g): 250.0
# Egg: 1.0
# Flour (g): 230.0
# ```
#     
# ***Write the code in the block below***

# In[6]:


n = int(input('How many cookies do you wish to make? '))
frac = float(n / 48)
print(frac)
print('Number of cookies: ', n)
print('Sugar (g): ', frac * 400)
print('Butter (g): ', frac * 320)
print('Chocholate (g): ', frac * 500)
print('Egg ', frac * 2)
print('Flour (g): ', frac * 230)


# #### Hint for task a: Escape Character

# `\n` is useful for forcing a new line! Example: `print(“hei\npå\ndeg”)` outputs
# 
# **print**
#   
# ```
# hei  
# på  
# deg
# ```

# ## b)

# Ask the user about how many cookies they want to make three times and print the ingredients in an elegant way (read: columns aligned correctly using spaces). You only need to print the number of cookies, as well as how much chocolate and sugar is needed. See the following example:
#  
# ```python
# How many cookies do you want to make? 24
# How many cookies do you want to make now?
# Lastly, how mny cookies do you want to make now? 72
#  
# Number of cookies:         sugar (g)       chocolate (g)
# 24                         200.0           250.0
# 48                         400.0           500.0
# 72                         600.0           750.0
# ```
# 
# `rjust()` og `ljust()` are useful functions here, but to use them you need to convert the number of cookies to a string using str().
# 
# ***Write the code in the block below.***

# In[10]:


a = int(input('How many cookies do you wish to make? '))
b = int(input('How many cookies do you wish to make now? '))
c = int(input('Lastly, how many cookies do you wish to make now? '))
f1 = a/48
f2 = b/48
f3 = c/48

print('Number of cookies:'.ljust(20), 'sugar (g)'.ljust(20), 'chocolate (g)'.ljust(20))
print(str(a).ljust(20), str(f1 * 400).ljust(20), str(f1 * 500).ljust(20) )
print(str(b).ljust(20), str(f2 * 400).ljust(20), str(f2 * 500).ljust(20) )
print(str(c).ljust(20), str(f3 * 400).ljust(20), str(f3 * 500).ljust(20) )


# #### `ljust()` and `rjust()`

# `streng.ljust(width)` tring.ljust(width) returns the string left justified in a string of length width. s strengen "left justified" i en streng av lengde width. streng.rjust(width) does the same, except the string is "right justified". For example `print('hei'.rjust(15))` outputs:
# 
#   
# ```python
#            hei      #text is printed after 12 white spaces as the string itself is 3 characters long.
# ```
#     
# Read more about `rjust()` og `ljust()` [here](https://docs.python.org/2/library/stdtypes.html?highlight=rjust#str.rjust). 

# In[ ]:




