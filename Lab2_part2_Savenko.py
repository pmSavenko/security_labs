#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Задача 2 (Алгоритм быстрого возведения в степень по модулю)
import numpy as np
import json
import math
import time

b = 4 
e = 13 
m = 497 
def pow_modul(b, e, m):
    if (m == 1): 
        return 0 
    c = 1
    for i in range(0, e):
        c = (c * b) % m
    return c

tm = time.clock()
res = pow_modul(b, e, m)
tm = time.clock() - tm
print('Расчет с помощью алгоритма быстрого  возведения в степень по модулю: '+'\n', '4^13 =', res, ' Time =', str(tm)+ '\n')

tm = time.clock()
res = pow(b, e) % m
tm = time.clock() - tm
print('Расчет с помощью встроенной функции pow: '+'\n', '4^13 =', res, ' Time =', str(tm)+ '\n')


# In[ ]:




