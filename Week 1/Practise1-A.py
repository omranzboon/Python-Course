#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name= input("enter your name : ")

x= int(input("Enter the first number : "))
y= int(input("Enter the seconed number : "))
greet = " Hi Mr/Mrs " 
print(greet + name +",")
print(f"The Sume of {x} and {y} is : {x+y}")
print(f"The Sub of {x} and {y} is  : {x-y}")
print(f"The Mul of {x} and {y} is  : {x*y}")
print(f"The Div of {x} over {y} is  : {x/y}")
print(f"The Reminder of {x} over {y} is {x%y}")
print(f"The Exponent of {x} to the Power of  {y} is {x**y}")

