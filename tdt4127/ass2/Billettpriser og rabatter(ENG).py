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
# 
# # Ticket Prices and Discounts
# 
# **Learning goals:**
# 
# * Conditions
# 
# **Starting Out with Python:**
# 
# * ch 3.1, 3.2, 3.4
# 
# 
# 314/5000
# In this assignment, you will use conditions (if-elif-else) to determine the ticket price of a user based on user input.
# 
# The transport company "TravelevatoR" offers train rides from Trondheim to Pythonville. If you book at least 14 days before you travel, you can get a minimum price 199. Regular ticket costs 440.

# ### a)

# Write a program that takes as input the amount of days to the travel date and outputs the availible price:
# 
# **Example run:**
#   
# ```
# Days to your trip? 15  
# You can have minimum price: 199,-  
# 
# 
# Days to your trip? 8  
# Too late for mimimum price; regular ticket: 440,-  
# ```
# ***Write your code below***

# In[2]:


day = int(input('Days to your trip? '))
if day >= 14:
    print('You can have minimum price: 199,-')
else:
    print('Too late for mimimum price; regular ticket: 440,-  ')


# ### b)

# Occasionally, customers do not want a mini-price, but rather want a full price ticket. This is because the mini-price cannot be refunded / changed. Therefore, expand the program so that customers are asked if they want a mini-price - but only where relevant. Two examples of driving after the expansion:
# 
#   
# ```python
# Days to trip? 17
# Mini-price 199,- cannot be refunded/changed
# Do you want this? (Y/N)? Y
# Jolly good! Have a nice trip.
# ```
#   
# ```python
# Days to trip? 17
# Mini-price 199,- cannot be refunded/changed
# Do you want this? (Y/N)? Y
# OK, you can have a regular ticket: 440,-
# ```

# In[5]:


day = int(input('Days to your trip? '))
if day >= 14:
    print('Mini-price 199,- cannot be refunded/changed') 
    val = input('Do you want this? (Y/N)? ')
    if val == 'Y':
        print('Jolly good! Have a nice trip.')
    elif val == 'N':
        print('OK, you can have a regular ticket: 440,-')
else:
    print('Too late for mimimum price; regular ticket: 440,-  ')


# ### c)

# It is decided that children under 16 are given a 50% discount. Seniors (60+), military in uniform, and students are given a 25% discount. For example, if the customer is both 60+ and military/student, it still gets only a 25% discount. All these discounts apply only in relation to full price (regular ticket), for the mini-price no discounts are given. Change the program so that it asks the customer about age and student/military, and calculates the correct price.
# 
# The new questions should only be asked ***when*** they are relevant, as it is a goal that the customer must answer as few questions as possible.
# 
# Example run:
# 
#   
# ```python
# Days to trip? 17
# Mini-price 199,- cannot be refunded/changed
# Do you want this? (Y/N)? N
# Age: 15
# You get the special price: 220,-
# ```

# In[8]:


day = int(input('Days to your trip? '))
if day >= 14:
    print('Mini-price 199,- cannot be refunded/changed') 
    val = input('Do you want this? (Y/N)? ')
    if val == 'Y':
        print('Jolly good! Have a nice trip.')
    elif val == 'N':
        age = int(input('Age: '))
        if age < 16: 
            print('You get the special price: 220,- ')
        elif age >= 60:
            print('You get the special price: 330,- ')
        else:
            case = input('Are you a student/military? (Y/N)? ')
            if case == 'Y':
                print('You get the special price: 330,- ')
            else:
                print('OK, you can have a regular ticket: 440,- ')
        
else:
    print('Too late for mimimum price; regular ticket: 440,-  ')        


# ### d) Voluntary task

# You will be approved if you have only completed a, b and part c, but try this a little harder d as well.
# 
# After heavy lobbying from student organizations, the rules are changed as follows: Students also get a little discount on mini-price tickets (10%), and that people who are both students and military / 60+, or students and children, receive two discounts, thus paying only 0.75 * 0.75 or 0.75 * 0.5 of full price. Note that people who are 60+ and military, but not students, or children and military, but not students, do not receive such a multiple discount, they still have to settle for the one discount they had before, and the usual 199 for the mini-price. Change the program to work properly in accordance with the new rules.

# In[ ]:




