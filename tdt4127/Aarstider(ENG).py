#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving2.ipynb">Assignment 2</a>
#     </div>
#   </div>
# </nav>
# 
# # Seasons
# 
# **Learning goals**
# - Conditions
# - Logical expressions
# 
# **Starting Out with Python:**
# - Kap. 3.3-3.5
# 
# In this assignment, a user must enter the day and month and find out what season the date belongs to.
# 
# One year has (officially) four seasons, and in this assignment we assume that the season changes follow the table below. 
# **(Note the dates) **
# 
# 
# Season | First day
# --- | ---
# Spring | 20. mar
# Summer | 21. jun
# Autumn | 22. sep
# Winter | 21. dec

# **Task:** Create a program that takes in a month as a string and a day in that month as a number from the user. The program will then print out the season associated with this date.
# 
# You can assume that the input is a valid date.
# 
# **Example run:**
# ```
# Month: mar
# Day: 20
# Spring
# ```  
#   
# ```
# Month: mar
# Day: 19
# Winter
# ```  
#   
# ```
# Month: nov
# Day: 20
# Autumn
# ```
# 
# ___Write your code here:___

# In[ ]:


mon = input('Month: ')
day = int(input('Day: '))
if mon == 'mar' :
    if day >= 20 : 
        print('Spring')
    else:
        print('Winter')
elif mon in [apr, may]:
    print('Spring')
elif mon == 'jun':
    if day < 21:
        print('Spring')
    else: 
        print('Summer')
    
elif mon in ['jul', 'aug']:
    print('Summer')
elif mon == 'sep':
    if day < 22:
        print('Summer')
    elif day >= 22: 
        print('Autumn')
        
elif mon in ['oct', 'nov']: 
    print('Autumn')
elif mon == 'dec':
    if day < 21:
        print('Autumn')
    else:
        print('Winter')


# In[ ]:




