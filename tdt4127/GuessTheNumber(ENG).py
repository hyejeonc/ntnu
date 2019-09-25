#!/usr/bin/env python
# coding: utf-8

# [Back to Assignment 3](_Oving3.ipynb)
# 
# # Guess the Number
# 
# **Learning goals**
# 
# * Loops
# * Conditions
# * Built-in functions
# 
# **Starting Out with Python:**
# 
# * Ch. 4.2-4.3
# 
# In this task, you will create a program that generates a random integer at a given interval, and then lets the user guess what that number is. This should be done using loops.
# 
# You will need to utilize the *random* library in python. In order to make it avalable in your program you need to start your code with ***import random***.
# 
# Example use of random.randint() (using the function randint() from the *random* library):
# 
# ```python
# randomNumber = random.randint(1,50)    # returns a random number between 1 and 50. (including 1 and 50)
# number = random.randint(a,b)           # returns a random number between a and b. 
# ```
# 
# 

# **a)** Ask the user to pick a lower and an upper limit for numbers to guess on. Save the two numbers in two different variables.
# 
# ***Write code in block below:***

# In[2]:


import random

a = int(input("Choose the lower limit : "))
b = int(input("Choose the upper limit : "))

RandomNum = random.randint(a, b)
CorrectNum = a - 1

while RandomNum != CorrectNum:
    CorrectNum = int(input("Make a guess : "))
    if CorrectNum > RandomNum:
        print("The correct number is higher!")
    elif CorrectNum < RandomNum:
        print("The correct number is lower!")
    else:
        print("You guessed correct!!!!!!!!!!!")
        break


# **b)**  Create a variable RandomNum that generates a random integer in the chosen interval, between the upper and lower bound. (continue in the code block from a))

# **c)** Write a WHILE-loop that runs for as long as the user guesses the wrong number. The user should get feedback for each guess on whether they guessed to low, to high or if they, in fact, guessed correctly.
# 
# Example run:
# ```python
# Give a lower bound for the random number: 1
# Give an upper bound for the random number: 100
# Make a guess 50
# The correct number is lower
# Make a guess 25
# The correct Number is higher
# Make a guess 37
# The correct number is lower
# Make a guess 32
# You guessed correct!```
