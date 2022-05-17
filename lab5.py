
# coding: utf-8

# In[14]:


import numpy as np
from sympy import *

p,q,r = symbols( 'p q r')
p = y+z
q = (x+z)
r = y+x

o = p*(q.diff(z)-r.diff(y))+q*(r.diff(x)-p.diff(z))+r*(p.diff(y)-q.diff(x))

if( o==0):
    print("Intergrable")
else:
    print("Not Intergrable")

