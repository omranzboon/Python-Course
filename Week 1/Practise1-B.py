#!/usr/bin/env python
# coding: utf-8

# In[4]:


x=float(input("Enter your number  ")) 

if x < -100 :
        result = -1*x 
        print(result)
elif  x>=-100 and x<= -25 :
        result = x**4
        print(result)
elif  x> -25 and x <= 0 :
        result = 3*(x**2) -1 
        print(result)
elif  x>0 and x<= 100:
        result = (22/14)*x +(3**x)
        print(result)
elif x>100 :
        result = x
        print(result)
    
    

