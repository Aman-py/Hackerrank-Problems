
# coding: utf-8

# In[2]:


n = int(input())
x = 123
if n > 123:
    while n >= x:
        print(x)
        x += 1
else:
    print(123)


# In[1]:


if __name__ == '__main__':
   n = int(input())
x = 4
if n > 3:
    while n >= x:
        print(123,x)
        x += 1
else:
    print(123)


# In[2]:


n = int(input())
animal_name = ""
all_animals = ""
animal_temp = ""
x = 3
if n > 3:
    while n > x:
        x += 1
        all_animals = animal_temp + animal_name
        animal_temp = all_animals
else:
    print(123)
print(all_num)


# In[1]:


print(*range(1, int(input()) + 1), sep="") 


# In[1]:


import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 


# In[2]:


tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
        # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("you win!")
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))

print("Game ended")
    


# In[1]:


check = input('enter your string or integer: '.title())
def str_analysis(check):
    while check = "":
        check
        


# In[2]:


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# In[1]:


L = range(1000)


# In[2]:


get_ipython().magic(u'timeit [i**2 for i in L]')


# In[2]:


import numpy as np


# In[21]:


a = np.array([(0,1),(1,2),(4,5),(6,7)])


# In[25]:


a


# In[11]:


-1 in range(10)


# In[12]:


timeit


# In[14]:


timeit(range(1))


# In[22]:


a.ndim


# In[23]:


a.shape


# In[20]:


len(a)


# In[24]:


len(a)


# In[26]:


b = np.array([[0, 1, 2], [3, 4, 5]])


# In[27]:


b.shape


# In[29]:


b.ndim


# In[30]:


len(b)


# In[31]:


range(b)


# In[32]:


hello = np.array([[[123], [567]], [[23], [49]]])


# In[34]:


hello.ndim


# In[35]:


c = np.array([[[1], [2]], [[3], [4]]])


# In[36]:


c.ndim


# In[37]:


hello.shape


# In[39]:


kadu = np.arange(10)


# In[40]:


kadu


# In[45]:


d = np.arange(-100,9,3)


# In[46]:


d


# In[51]:


e = np.linspace(1,5,10,endpoint = False)


# In[52]:


e


# In[62]:


f = np.ones((0,3))


# In[63]:


f


# In[73]:


g = np.zeros((4,3,2,6))


# In[74]:


g


# In[84]:


h = np.eye(4,3)


# In[85]:


h


# In[90]:


i = np.diag(np.array([(1,1,1,1), 2, 3, 4,5]))


# In[91]:


i


# In[94]:


j = np.random.rand(100)


# In[95]:


j


# In[98]:


k = np.random.randn(100)


# In[99]:


k


# In[100]:


l = np.random.seed(1234)  


# In[101]:


l


# In[102]:


a.dtype


# In[109]:


m = np.array([1.,3,4.,5])


# In[110]:


m.dtype


# In[111]:


e.dtype


# In[5]:


n = np.array(input())


# In[7]:


n


# In[8]:


o = np.array(True)


# In[10]:


o.dtype


# In[12]:


p = np.array(3 > 5)


# In[13]:


p


# In[15]:


q = np.array([1 + 2j])


# In[16]:


q


# In[17]:


q.dtype


# In[18]:


r = np.array(['hello','python',3,True])


# In[19]:


r


# In[20]:


s = np.array(['harry','potter','ron','hermayni'])


# In[21]:


s


# In[22]:


s.dtype


# In[43]:


import matplotlib.pyplot as plt


# In[54]:


x = np.linspace(0,10,20)
y = np.linspace(0,10,20)
plt.plot(x,y,'o')


# In[55]:


plt.show(x,y)


# In[60]:


ab = (10,10)
bc = (0,5)
plt.plot(ab,bc,'r')


# In[61]:


plt.show(ab,bc)


# In[67]:


image = np.random.rand(30, 30)


# In[68]:


plt.imshow(image, cmap=plt.cm.hot)


# In[69]:


plt.colorbar()


# In[70]:


plt.show()


# In[72]:


r = np.arange(10)


# In[73]:


r[0]


# In[74]:


r[0],r[9]


# In[75]:


r[0],r[-2]


# In[77]:


r[::9]


# In[78]:


r[::-1]


# In[80]:


r[::-2]


# In[81]:


r


# In[ ]:




