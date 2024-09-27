#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[3]:


if 5>3:
print("Wrong identification")


# In[6]:


if 5>3:
    print("Right identification")


# In[7]:


#this is a comment
print("comment test")


# In[8]:


#this is a comment
#python doesn not have multiline comment
print("comment test")


# In[10]:


a = 5
b = 6.0098
_car = 'BMW' #can use '' or " "

print(_car)
print(b)
print(a)


# In[12]:


#value assigned to multiple variables
car1, car2, car3 = "BMW","Mercedes","Volkswagen"
print(car1)
print(car2)
print(car3)


# In[13]:


car1=car2=car3="Viva"
print(car1)
print(car2)
print(car3)


# In[14]:


nama = 'Dan'
print('My name is ' + nama)


# In[15]:


nama = 'Dan'
ayat = 'My name is '
print( ayat + nama)


# In[16]:


number1 = 20
number2 = 2020
print(number1+number2)


# In[17]:


location = 'Sungai Petani'
def function1():
    print(location)
function1()


# In[18]:


location = 'Sungai Petani'
def function1():
    location='Jitra'
    print(location)
function1()
print(location)


# In[19]:


location = 'Sungai Petani'
def function1():
    global location
    location='Jitra'
    print(location)
    
function1()
print(location)


# In[20]:


e = ["wij", "dan", "mohamad"]
print(e)
print(type(e))


# In[23]:


f = ("wij", "dan", "mohamad")
print(f)
print(type(f))


# In[24]:


e = ["wij", "dan", "mohamad"]
print(e)

e[2]='ariff'
print(e)


# In[25]:


f = ("wij", "dan", "mohamad")
print(f)
f[2]=ariff
print(f)


# In[34]:


e = ["wij", "dan", "mohamad"]
f = ("wij", "dan", "mohamad")

print(e.__sizeof__())
print(f.__sizeof__())


# In[29]:


h = {'name': 'wijdan', 'age':20}
print("his name is", h['name'])
print("his age is", h['age'])


# In[32]:


print(1,2,3,4)
print(1,2,3,4, sep='#', end='.')


# In[33]:


x=10
y=2020
print("I am {} years old in {}".format(x,y))


# In[35]:


print("i love {0} and {1}".format("Omar", "Haz"))
print("i love {1} and {0}".format("Omar", "Haz"))


# In[36]:


z = input('Enter a number: ')
z


# In[37]:


name, age = input('enter your name: '), int(input('enter your age '))


# In[39]:


x=2
y=4
print("x + y = ", x+y)
print("x - y = ", x-y)
print("x * y = ", x*y)
print("x / y = ", x/y)
print("x // y = ", x//y)
print("x ** y = ", x**y)


# In[40]:


x=2
y=4
print("x > y = ", x>y)
print("x < y = ", x<y)
print("x == y = ", x==y)
print("x != y = ", x!=y)
print("x >= y = ", x>=y)
print("x <= y = ", x<=y)


# In[45]:


x= True
y= False
print("x and y = ", x>y)
print("x or y = ", x<y)
print("x and y = ", x==y)


# In[50]:


x = 8
y = 4

print(x&y)
print(x|y)
print(~x)
print(x^y)
print(x>>y)
print(x<<y)


# In[52]:


z = input('Enter a number: ')
z


# In[ ]:


name, age = input('enter your name: '), int(input('enter your age '))


# In[ ]:




