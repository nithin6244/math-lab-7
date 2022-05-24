
# coding: utf-8

# In[2]:


#Type 1

from sympy.abc import x,y,a,b,c
from sympy import *
f = Function('f')
u = f(x,y)
p = u.diff(x)
q = u.diff(y)
eq = p**2+q**2-1
Eq = eq.subs(p,a).subs(q,b)
print("Equation becomes ", Eq)
b_val = solve(Eq,b)
print("b = ",b_val)
z = a*x+b*y+c
ans = z.subs(b,b_val[0])
print("The required solution is ",ans)


# In[6]:


#Type 1

from sympy.abc import x,y,a,b,c
from sympy import *
f = Function('f')
u = f(x,y)
p = u.diff(x)
q = u.diff(y)
eq = p*q
Eq = eq.subs(p,a).subs(q,b)
print("Equation becomes ", Eq)
b_val = solve(Eq,b)
z = a*x+b*y+c
ans = z.subs(b,b_val[0])
print("The required solution is ",ans)


# In[37]:


#Type 1

from sympy.abc import x,y,a,b,c
from sympy import *
f = Function('f')
u = f(x,y)
p = u.diff(x)
q = u.diff(y)
eq = p*q+q+p
Eq = eq.subs(p,a).subs(q,b)
print("Equation becomes ", Eq)
b_val = solve(Eq,b)
z = a*x+b*y+c
ans = z.subs(b,b_val[0])
print("The required solution is ",ans)


# In[16]:


#Type 2

from sympy import Function, diff, Eq, pprint,solve,dsolve
from sympy.abc import x,y,u,p,q,a,b
z = Function('z')(u)
eqn = p*(1-q**2)-q*(1-z)
eqn1 = eqn.subs(p,diff(z,u)).subs(q,a*diff(z,u))
h1 =solve(eqn1,diff(z,u))
sol = dsolve(h1[0]-diff(z,u))
ans = sol.subs(u,x+a*y)
print("Required solution is ")
print(ans)


# In[38]:


#Type 2

from sympy import Function, diff, Eq, pprint,solve,dsolve
from sympy.abc import x,y,u,p,q,a,b
z = Function('z')(u)
eqn2 = p*(1+q)-z*q
eqn3 = eqn2.subs(p,diff(z,u)).subs(q,a*diff(z,u))
h1 =solve(eqn3,diff(z,u))
sol = dsolve(h1[0]-diff(z,u))
ans = sol.subs(u,x+a*y)
print("Required solution is ")
print(ans)


# In[19]:


#type 2

from sympy import Function, diff, Eq, pprint,solve,dsolve
from sympy.abc import x,y,u,p,q,a,b
z = Function('z')(u)
eqn = p-q*z
eqn1 = eqn.subs(p,diff(z,u)).subs(q,a*diff(z,u))
h1 =solve(eqn1,diff(z,u))
sol = dsolve(h1[0]-diff(z,u))
ans = sol.subs(u,x+a*y)
print("Required solution is ")
print(ans)


# In[28]:


#Type 3

from sympy.abc import x,y,k,a,b,c
from sympy import *
lhs = p+x
rhs = q+y
r1 = Eq(lhs,a)
r2 = Eq(rhs,a)
h1 = solve(r1,p)
h2 = solve(r2,q)
z = integrate(h1[0],x)+integrate(h2[0],y)
print("The solution is ",z)


# In[29]:


#Type 3

from sympy.abc import x,y,k,a,b,c
from sympy import *
lhs = p-cos(x)
rhs = q*cos(y)
r1 = Eq(lhs,a)
r2 = Eq(rhs,a)
h1 = solve(r1,p)
h2 = solve(r2,q)
z = integrate(h1[0],x)+integrate(h2[0],y)
print("The solution is ",z)


# In[31]:


#Type 3

from sympy.abc import x,y,k,a,b,c
from sympy import *
lhs = p-sin(x)
rhs = sin(y)-q
r1 = Eq(lhs,a)
r2 = Eq(rhs,a)
h1 = solve(r1,p)
h2 = solve(r2,q)
z = integrate(h1[0],x)+integrate(h2[0],y)
print("The solution is ",z)


# In[33]:


from sympy.abc import x,y,k,a,b,c
from sympy import *
z = p*x+q*y+(p**2-q**2)
sol = z.subs([(p,a),(q,b)])
print("Solution is ",sol)


# In[35]:


from sympy.abc import x,y,k,a,b,c
from sympy import *
z = p*x+q*y+(p*q)/(p-q)
sol = z.subs([(p,a),(q,b)])
print("Solution is ",sol)


# In[36]:


from sympy.abc import x,y,k,a,b,c
from sympy import *
z = p*x+q*y+log(p*q)
sol = z.subs([(p,a),(q,b)])
print("Solution is ",sol)

