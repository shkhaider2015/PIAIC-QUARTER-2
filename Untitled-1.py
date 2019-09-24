# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
from IPython import get_ipython


#%%
import numpy as np


#%%
list1 = [1, 3, 4, 5]
a = np.array(list1)
a


#%%
type(a)


#%%
a.dtype


#%%
a.size


#%%
a.ndim


#%%
a.shape


#%%
b = np.array([23, 7.4, 11, 98, 54, 23.67])
type(b)


#%%
b.ndim


#%%
b.size


#%%
b.shape

#%% [markdown]
# ## Indexing and Slicing

#%%
c = np.array([22, 56, 98, 54, 21])
c


#%%
#assign 56 to 34
c[1] = 34
c


#%%
# slicing
d = c[1:3]
d


#%%
d[0:2] = 66, 77
d

#%% [markdown]
# ## Basic operation
#%% [markdown]
# ### Vector Addition and subtraction

#%%
v1 = np.array([0, 1])
v2 = np.array([1, 0])
v1 + v2


#%%
## anothr way
u = np.array([1, 0])
v = np.array([0, 1])
z = []

for n,m in zip(u, v):
    z.append(n+m)
z

#%% [markdown]
# ### Array multiplication with scaler

#%%
y = np.array([1, 2])
z = 2*y
z


#%%
## another way
zz = []
for n in y:
    zz.append(2*n)
zz

#%% [markdown]
# ### Product of two vectors

#%%
tt1 = np.array([1, 2])
tt2 = np.array([3, 4])

tt = tt1 * tt2
tt


#%%
## another way
tt3 = []
for n,m in zip(tt1, tt2):
    tt3.append(n*m)
tt3

#%% [markdown]
# ### Dot product

#%%
ff1 = np.array([1, 2])
ff2 = np.array([3, 4])

result = np.dot(ff1, ff2)
result


#%%
## another way
result2 = []
for n,m in zip(ff1, ff2):
    result2.append(np.dot(n, m))
result2

#%% [markdown]
# ### Adding constant to numpy array
#%% [markdown]
# 

#%%
gg = np.array([2, 3, 4, -9])
res1 = gg + 1
res1

#%% [markdown]
# ## Universal Function

#%%
fg = np.array([3, 5, 7, 9])


#%%
fg.mean()


#%%
fg.max()


#%%
fg.min()


#%%
## pi value
np.pi


#%%
# np.sin(x)
# 
#


#%%
# starting value = -2 and ending value= 2 total values 5
np.linspace(-2, 2, num=5)


#%%
np.linspace(-2, 2, num=9)


#%%
## plotting mathamatical function
x = np.linspace(0, 2*np.pi, 50)
x


#%%
y = np.sin(x)
y


#%%
import matplotlib.pyplot as plt


#%%
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x, y)
#first input x is horizontal axis
#second element y is vertical axis

#%% [markdown]
# # Two Dimenstional Array

#%%
a = np.array([[1, 2, 3], [11, 12, 13], [21, 22, 23], [31, 32, 33]])


#%%
a.ndim


#%%
a.shape


#%%
a.size


#%%
# to access first row 3rd element
a[0][2]


#%%
# alternate
a[0, 2]


#%%
## slicing in numpy array
a[0, 0:2]


#%%
## adding as matrix
as1 = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 3, 5, 7]
])
as2 = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 3, 5, 7]
])


#%%
as1 + as2


#%%
as1.ndim


#%%
as1


#%%
as1 * 2


#%%
# matrix multiplication is littile bit complex
# matrix A rows must b equal to matrix B column
# each element of A is multiply with all element of B column


#%%
dfA = np.array([[1, 2, 3], [2, 0, 1]])
dfB = np.array([[1, 2], [0, 1], [3, 4]])


#%%
dfZ = np.dot(dfA, dfB)


#%%
dfZ


#%%
X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
Z


#%%



