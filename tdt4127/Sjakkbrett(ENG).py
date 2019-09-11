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
# # Chess
# 
# **Learning goals:**
# 
# * Conditions
# * Logical expressions
# * Nested if-conditions
# 
# **Starting Out with Python:**
# 
# * Kap. 2.7
# * Kap. 3.2-3.3
# * Kap. 3.5
#  
# Chessboard positions can be identified by a letter and a number. The letter identifies the column (called the "line" in chess), and the number identifies the row.
# 
# 
# ![img](./../../Resources/Images/chessboard.png)
# 

# ### a)

# **In this task, create a program that takes a position from the user and uses if statements to determine the color of the route for that position.**
# 
# Take a look at the three code lines below, which will help you along the way. These show how to use indexing of a string variable (named `pos`) to find single characters.
# 
# Index 0 is the first character of the string, when `pos = 'a5'`, `pos[0]` will be `'a'` and `pos[1]` will be`'5'`.
# 
# In your code you will need to
# 
# * Change the line with `position = 'a5'` with a line of code which asks the user to input a position
# * add more code below the line `number = ...` in order to make a decision whether the given position is a white or black square.
# 
# Example run:
# 
#   
# ```
# Position: a5  
# Black 
# ```
#   
# ```
# Position: d3  
# White
# ```
#   
# ```
# Position: f6
# Black
# ```

# In[4]:


pos = input('Position: ')  # use input() to get the positon from the user
 
letter = pos[0]                # gives the variable 'letter' the value 'a' (in this example)
number = int(pos[1])              #gives the variable 'number' the value 5
  
# Add more code here
if letter in ['a', 'c', 'e', 'g']:
    if number % 2 == 0: 
        print('White')
    else:
        print('Black')
else:
    if number % 2 == 0: 
        print('Black')
    else:
        print('White')


# #### Hint

# Modulo (`%`)

# ## b) Voluntary(!) challenging task

# You do not need to have this task (b) approved for the assignment.
# 
# **Expand the program so that it also handles possible incorrect user input, as follows**:
# * If the user writes a string with length other than two characters (shorter or longer), the program should print `"Wrong input, you need to input exactly two characters"`, then stop.
# * If the given input is 2 characters long but not "belonging" to a square in a chess board, the program should output as shown below. To clarify, this should happen if the first character is NOT a letter in the range A to H (a to h) and/or the second sign is NOT a number in the range 1 to 8.
# 
#   
# ```
# Position: A9
# Wrong input.
# First character needs to be a letter A-H or a-h
# Second character needs to be a number 1-8
# ```
# 
# If the input is in the correct format and inside the allowed ranges, the program should output the same as in task a)

# In[ ]:




