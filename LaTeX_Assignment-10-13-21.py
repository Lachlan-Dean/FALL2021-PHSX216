#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Rule 1
import numpy as np

def rule1(c, da):
    dQ = c*da
    return dQ
d1 = 0.005
c = 9.8
errd1 = 0.0005
df = c*d1
errdf = rule1(c,errd1)

print("df =", df)
print("errdf =", errdf)


# In[2]:


#Rule 2
import numpy as np

def rule2(dA, A, Q, m):
    dQ = Q*(m*(dA/A))
    return dQ
a = 0.06
da = 0.0005
M = 2
q = 5
errq = rule2(da, a, M, q)

print("q = ", q)
print("errq =", errq)


# In[3]:


#Rule 3
import numpy as np

def rule3(da, db):
    dQ = np.sqrt(da**2+db**2)
    return dQ

d1 = 1.0
d2 = 0.3
errd1 = 0.0005
errd2 = 0.0005
dtotal = d1 + d2
errdtotal = rule3(errd1, errd2)
print("dtotal =", dtotal)
print("errdtotal =", errdtotal)


# In[5]:


#Rule 4
import numpy as np

def rule4(A, dA, m, B, dB, n, Q):
    
    dQ = Q*np.sqrt((m*(dA/A))**2+((n*(dB/B))**2))
    
    return dQ

y = .99
xavg = 1.57
erry = 0.0005
errx = .0055
g = 9.81
m = 1
n = 1

vi = xavg*np.sqrt(g/(2*y))
errvi = rule4(y, erry, m, xavg, errx, n, vi)

print("vi = ", vi)
print("errvi = ", errvi)
print("There was a slight error in our lab calculations of vi, the number we calculated was 3.509 ")


# In[6]:


#Mean and Error in Mean
x = np.array([ 1.1, 1.3, 1.4, 0.9, 0.95, 1.05])
xmean = np.average(x)
xstdev = np.std(x)
n = x.size
errxmean = xstdev/np.sqrt(n)

print ("The mean of the data set is: ", xmean)
print ("The error in the mean is: ", errxmean)


# Rule 3:
# 
# $\delta Q = \sqrt{(\delta A)^2+(\delta B)^2}$
# 
# Rule 4:
# 
# $\delta v_i = v_i\sqrt{(\frac{\delta x}{x})^2+(\frac{\frac{-1}{2}\delta y}{y})^2}$

# In[ ]:




