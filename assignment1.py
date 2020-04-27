#!/usr/bin/env python
# coding: utf-8

# TASK 1:

# In[1]:


numbers=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        numbers.append(i)
print(numbers)        
        


# In[2]:


x=input("enter the first name ")
y=input("enter the last name ")
print(y+" "+x)


# In[3]:


r=12
V=((4/3)*3.141593*r**3)
print(V)


# TASK 2:

# In[4]:


x=input("enter the sequence of comma-seperated numbers")
y=list(x)
print(y)


# In[6]:


for i in range(1,10):
    if i not in range(6,11):
        print("*"*i)
    else:
        j=10-i
        print("*"*j)
    
    
    
    


# In[9]:


x=input("enter the input word ")
print(x[::-1])

