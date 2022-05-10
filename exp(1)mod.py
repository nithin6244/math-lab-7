
# coding: utf-8

# In[3]:


import numpy as np
from numpy import linalg as la

def T(x,y,z):
    return [x-y+z,2*x+3*y+(0.5)*z,x+y-2*z]

B1 = np.array([[-1,1,0],[5,-1,2],[1,2,1]])
print("The specifeid basis fdor the domain space is ", B1)
B2 = np.array([[1,1,0],[0,0,1],[1,5,2]])
print("The specifeid basis fdor the domain space is ", B2)


w1 = T(-1,1,0)
w2 = T(5,-1,2)
w3 = T(1,2,1)

print("Evaluating T at the vectors of basis B1 : ",w1,w2,w3)

v1 = la.solve(B2.T,w1)
v2 = la.solve(B2.T,w2)
v3 = la.solve(B2.T,w3)

M= np.array([v1,v2,v3])

print("The matrix of the linear transformation id : \n",M.T)

