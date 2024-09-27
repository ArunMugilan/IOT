#!/usr/bin/env python
# coding: utf-8

# In[2]:


value =int(input('enter a number: '))

if value >0:
    print('positive number')
elif value ==0:
    print('zero')
else:
    print('negative number')


# In[4]:


car = ['BMW', 'Merc', 'Proton']
for x in car:
    print(x)


# In[6]:


for x in 'Mercedes':
    print(x)


# In[18]:


a=1
b=10
while a<b:
    print ('a lower than b')
    a=a+1


# In[20]:


def my_fuction():
    """This function to print hello"""
    print('Hello')

my_function()


# In[14]:


def my_fuction():
    a=int(input('a:'))
    b=int(input('b:'))
    print(a+b)

my_function()


# In[17]:


def check_fever():
    temperature = float(input("Enter your body temperature: ")) 
    
    if temperature >= 38.0:
        print("You have a fever.")
    else:
        print("You are healthy.")

# Call the function
check_fever()

