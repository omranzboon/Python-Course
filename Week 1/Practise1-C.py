#!/usr/bin/env python
# coding: utf-8

# In[ ]:


y=input("Please enter your temperature type for Celsius input enter c, for Fahrenheit input enter f  ")
x= float(input(" Please enter your temperature value "))

if y =="f" or y =="F" :
     t = (x-32)/1.8 
     print(t)   
            
elif y =="c" or y=="C" :
     t= (x*1.8) +32
     
     print(t)

