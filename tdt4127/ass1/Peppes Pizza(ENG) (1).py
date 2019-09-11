#!/usr/bin/env python
# coding: utf-8

# 
# # Peppes Pizza (ENG)
# 
# 
# 
# **Learning goals**
# - Performing simple calculations in Python
# - Writing a simple program in Python
# 
# **Starting Out with Python:**
# 
# * ch. 2
# 
# 
# 
# You have recently eaten dinner at Peppes Pizza with a couple of your friends, and you receive the following receipt:
# ```python
# Pizza: 750kr
# Student discount: 20%
# Tip: 8%
# ```

# ## a)

# Write a program which stores the values from the receipt as variables. The variables should be `pizza`, `discount` and `tip`. 
# 
# ***Write the code in the block below***

# In[11]:


pizza = 750
discount = 0.20
tip = 0.08


# #### Similar Example

# Bob Bernt was at the cinema during the weekend and received the following receipt:
# 
# **Receipt from Prinsen Cinema:**
#   
# ```python
# Movie ticket: 125kr
# Popcorn: 70kr
# Soda: 25kr
# Discount = 10%
# ```
# 
# In the following program, the values from the receipt have been stored in the values `ticket`, `popcorn` and `soda`.
# 
# **Code:**
# 
#   
# ```python
# ticket = 125
# popcorn = 70
# soda = 25
# discount = 0.10
# ```

# ## b)

#  Create the variable `total`, which should be equal to the total price for the dinner.

# In[14]:


total = pizza * (1 - discount) + pizza * tip
print(total)


# #### Similar Example

# Based on the receipt from Prinsen Cinema, which Bob Bernt received under Example of a similar case in Task A. Computing the total sum can be done as follows:
# 
#   
# ```python
# total = (ticket + soda + popcorn) * (1 - discount)
# ```

# ## c) 

# Expand the program such that the user can enter how many people participated at the dinner, and output how much each person has to pay.
# 
# **Eksempel på kjøring:**
# 
#   
# ```python
# Total price: 648.0
# How many people participated at the dinner? 6
# Since you were 6 persons, so each person has to pay 108.0 kroner.
# ```
# 
# ***Write the code in the block below***

# In[15]:


print('Total price: ', total)
n = int(input('How many people participated at the dinner? '))
print('Since you were ', n, 'people, so each person has to pay ', total/n, 'kroner.')


# ### Hint

# To use input in computations, the user input must be converted to an int.

# In[ ]:




