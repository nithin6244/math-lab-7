
# coding: utf-8

# In[6]:

#Finding The matrix of Teh linear transformation


import numpy as np
from numpy import linalg as la

def T(x,y,z):
    return [x-y+z,2*x+3*y+(0.5)*z,x+y-2*z]

B1 = np.array([[-1,1,0],[5,-1,2],[1,2,1]])
print("The specifeid basis fdor the domain space is ", B1)
B2 = np.array([[1,1,0],[0,0,1],[1,5,2]])
print("The specifeid basis fdor the domain space is ", B2)


v1 = T(-1,1,0)
v2 = T(5,-1,2)
v3 = T(1,2,1)

print("Evaluating T at the vectors of basis B1 : ",v1,v2,v3)

v1 = la.solve(B2.T,v1)
v2 = la.solve(B2.T,v2)
v3 = la.solve(B2.T,v3)

M= np.array([v1,v2,v3])

print("The matrix of the linear transformation id : \n",M.T)


# In[4]:

#Finding linear transformation when matrix and the basis are given :


from sympy import symbols, Matrix,solve
import numpy as np

a,c1,c2,x,y = symbols("a c1 c2 x y")

A = Matrix([[2,3],[4,-5]])

u1 = np.array([1,-1])
u2 = np.array([1,1])
v1 = np.array([1,0])
v2 = np.array([0,1])

T0 = [A[0,0]*v1,A[1,0]*v2]
T1 = [A[0,1]*v1,A[1,1]*v2]

sumTo = T0[0] + T0[1]
sumT1 = T1[0] + T1[1]

print("The image of the ordered basis vector in B1 under the transformation are ",sumTo,sumT1)

eq = np.array([u1[0]*c1+u2[0]*c2,u1[1]*c1+u2[1]*c2])

p, q = eq[0],eq[1]

a = solve((p-x,q-y),c1,c2,dict = True)

c1,c2 = a[0][c1],a[0][c2]

print("The cordinates of vectoers (x,y) w.r.t B1 are ",c1,"and",c2)

t = sumTo*c1 +sumT1*c2

print("The Lt of T is T(x,y) = ",tuple(t))

