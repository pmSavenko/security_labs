#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Задача 1 (Модульная арифметика)
#В системе модулей (3, 5, 7) сложить и умножить числа 14 и 8
import numpy as np
import math

x1 =14
x2 = 8
p = np.array([3, 5, 7])

A_x1 = np.zeros(len(p), dtype=int)
A_x2 = np.zeros(len(p), dtype=int)
A_Sum = np.zeros(len(p), dtype=int)
A_Multip = np.zeros(len(p), dtype=int)

def return_num(A_x, p):
    M_multi = 1
    for i in range (0, len(p)):
        M_multi *= p[i]
    M = np.array(M_multi/p, dtype=int)
    b = np.zeros(len(p), dtype=int)
    for i in range (0, len(p)):
        j=1
        while ((p[i]*j+1)%M[i]!=0):
            j += 1
        b[i]=(p[i]*j+1)/M[i];
    X = sum(A_x*(M*b))% M_multi
    return(X)   

for i in range (0, len(p)):
    A_x1[i] = x1 % p[i] 
    A_x2[i] = x2 % p[i] 
print('Представим числа Х1 =', x1,' и X2 =', x2,' в системе модулей', p,':')
print('X1 =', A_x1)
print('X2 =', A_x2)

for i in range (0, len(p)):
    A_Sum[i] =  (A_x1[i]+A_x2[i])% p[i] #суммирование
    A_Multip[i] =  (A_x1[i]*A_x2[i])% p[i] #перемножение
print('X1+X2 =', A_Sum)
print('X1*X2 =', A_Multip)
print('Возвращаемые значения: ')
print('X1 =',return_num(A_x1, p),'X2 =',return_num(A_x2, p))
print('X1+X2 =', return_num(A_Sum, p))
print('X1*X2 > 105')
#print('X1*X2 =', return_num(A_Multip, p))


# In[21]:


print('Проверка:')
A_Y1 = np.zeros(len(p), dtype=int)
A_Y2 = np.zeros(len(p), dtype=int)
Y1 = x1+x2
Y2 = x1*x2
for i in range (0, len(p)):
    A_Y1[i] = Y1 % p[i] 
    A_Y2[i] = Y2 % p[i] 
print('X1+X2 =', Y1, '=', A_Y1)
print('X1*X2 =', Y2, '=', A_Y2)


# In[ ]:




