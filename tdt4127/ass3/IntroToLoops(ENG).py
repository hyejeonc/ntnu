#!/usr/bin/env python
# coding: utf-8

# [Back to Assignment 3](_Oving3.ipynb)
# 
# # Introduction to loops
# 
# **Learning objectives:**
# 
# * Loops
# * Choosing the appropriate loop type (FOR and WHILE)
# 
# **Starting Out with Python:**
# 
# * Ch. 4.1-4.3
# 
# In this exercise you will learn how loops function, why we use them, as well as how they function in Python.

# ### Introduction to loops

# Loops allow us to write code that can be run several times, without having to repeat the same lines of code.
# In the example below, we have written the same line three times in a row:

# In[ ]:


print("Hipp")
print("Hipp")
print("Hipp")
print("Hurra!")


# We can write the same output using a FOR-loop:

# In[ ]:


for i in range(3):
    print("Hipp!")
print("Hurra!")


# for < variable > in range(3): ensures that the following code line that is indented is run three times, saving us the hassle of writing the same exact line of code three times in a row. Consider if we were to output the same a million times in a row, instead of just three. The benefit of using a loop should be obvious. 
# 
# The code line `print("Hurra!")` which is not indented, is not a part of loop, and will thus be executed just once, after the loop.
# 
# 
# There are two types of loops in Python - FOR and WHILE. Instead of a FOR-loop, we could have used a WHILE-loop instead. We could then write the code as:

# In[ ]:


i = 0
while i < 3:
    print("Hipp")
    i = i + 1  #  # or instead: i += 1
print("Hurra!")


# WHILE is a bit more cumbersome in this situation, we have to explicitly increase the counter i with one for each iteration, which is rather defined implicitly for the previous example code with FOR. 
# 
# The WHILE-loop will continue to run as long as the condition (i < 3) is true, it will therefore run while i is 0, 1, 2, but stops when i is increased to 3. As with the FOR-loop, this ensures that "Hipp" is written thrice.
# 

# ## a)

#  The code below shows a FOR-loop that is run three times. For each iteration the user is asked to describe themselves with an adjective, upon which the machine gives an appropriate response.
# 
# (The trick here is to add "er" behind the adjective)
# 
# Run the code to see how it functions.
# 
# ***Now change the code such that the program first asks the user how many iterations they wish to run, the program should then run the above code that many times..***
# 
# Example run:
# 
# ```
# How many iterations? 2
# Describe yourself with an adjective: nice
# Bah, you nice!? I am nicer!
# Describe yourself with an adjective: strong
# Bah, you strong!? I am stronger!
# Goodbye!
# ```

# In[3]:


# Change the code below
n = int(input("How many iterations? "))

for i in range(n):
    adj = input("Describe yourself with an adjective: ")
    print("Bah, you", adj + "!? I am ", adj + "er!")
print("Goodbye!")


# #### Hint

# Instead of the number 3 in the code, this should be replaced with a variable that takes in an input from the user (use the input()-function).

# ## b)

# The code below shows a WHILE-loop that is equivalent to the code from (a), with 3 iterations. Copy the code into your editor and run it to see how it functions.
# **Now change the code such that it has not only 3 iterations, but lets the user choose the amount of iterations. The code will run for as long as the user inputs answers, and exits when the user presses Enter without inputting an answer. The input()-function will thus return an empty string, "**.
# 
# Example run
# 
# ```
# Press enter without inputting an answer to exit.
# Describe yourself with an adjective: nice
# Bah, you nice!? I am nicer!
# Describe yourself with an adjective: strong
# Bah, you strong!? I am stronger!
# Describe yourself with an adjective: great
# Bah, you great!? I am greater!
# Describe yourself with an adjective:
# Goodbye!
# ```
# 
# The fourth time the answer was asked, the user just pressed Enter without inputting an answer. The program, resultingly, exited.

# In[ ]:


i = 0
while i < 3:
    adj = input("Describe yourself with an adjective: ")
    print("Bah, you", adj + "!? I am ", adj + "er!")
    i += 1  # increases i with 1
print("Goodbye!")


# ## c)

# Use the code with the WHILE-loop with 3 iterations from (b). Now change the code as follows:
# 
# The user starts with 42 alphabetic characters available to them. For each iteration the program should decrease this number by the amount of characters in the adjective inputted.
# 
# the loop should run as long as this number is above zero. 
# 
# **Example run:**
# 
# ```
# You have 42 letters remaining.
# Describe yourself with an adjective: nice
# Bah, you nice!? I am nicer!
# You have 38 letters remaining.
# Describe yourself with an adjective: strong
# Bah, you strong!? I am stronger!
# You have 32 letters remaining.
# Describe yourself with an adjective: understanding
# Bah, you understanding!? I am understandinger!
# You have 19 letters remaining.
# Describe yourself with an adjective: smashing
# Bah, you smashing!? I am smashinger!
# You have 9 letters remaining.
# Describe yourself with an adjective: trivial
# Bah, you trivial!? I am trivialer!
# You have 1 letters remaining.
# Describe yourself with an adjective: E
# Bah, you E!? I am Eer!
# You have 0 letters remaining.
# Goodbye!
# >>>
# ```

#  ## d)

# In the code below, the first two FOR-loops are complete, but the following three is not. Change range(0) i these loops such that it runs the number of iterations corresponding to the above print()-statement.

# In[7]:


print("Odd numbers from 1 to 20:")
for number in range(1, 20, 2):
    print(number, end = " ")
print()
  
print("Every third number from 12 to 25:")
for number in range(12, 25, 3):
    print(number, end = " ")
print()
  
print("Every fifth number from 20 to 81:")
for number in range(20, 81, 5):
    print(number, end = " ")
print()
  
print("The number sequence 48, 56, 64, 72, 80")
for number in range(48, 81, 8):
    print(number, end = " ")
print()
  
print("Count backwards from 100 to 80, with an interval of -3, eg. 100, 97, ...:")
for number in range(100, 80, -3):
    print(number, end = " ")
print()


# ## e)
# Make a program that prints the numbers 1 to 5 with a FOR-loop

# In[8]:


for number in range(1, 6, 1):
    print(number, end = " ")
print()


# ## f) 
# Make a program that prints the numbers starting from 15 to 1 with a FOR-loop

# In[12]:


for number in range(15, 0, -1):
    print(number, end = " ")
print()


# In[ ]:




