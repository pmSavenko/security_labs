#!/usr/bin/env python
# coding: utf-8

# In[73]:


import random
import json
import math
import time

A = [random.randint(0, 100000) for i in range(1, 50)]
with open('array50.txt', 'w') as af:
    json.dump(A, af)

A = [random.randint(0, 100000) for i in range(1, 200)]
with open('array200.txt', 'w') as af:
    json.dump(A, af)

A = [random.randint(0, 100000) for i in range(1, 1000)]
with open('array500.txt', 'w') as af:
    json.dump(A, af)


# In[74]:


def LinearSearch(ar, element):
    for i in range (len(ar)):
        if ar[i] == element:
            return i
    return -1


# In[75]:


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


# In[76]:


def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1


# In[86]:


with open('array50.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[21]
tm = time.clock()
res = LinearSearch(sa, mynum)
tm = time.clock() - tm 
print('\n Результаты для массива 50\n')
print('   Индекс: ' + str(res) + '\n')
print(' Время выполнения линейного поиска: ' + str(tm)+ '\n')

with open('array50.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[21]
tm = time.clock()
res1 = BinarySearch(sa, mynum)
tm = time.clock() - tm 
print(' Время выполнения бинарного поиска: ' + str(tm)+ '\n')


with open('array50.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[21]
tm = time.clock()
res1 = FibonacciSearch(sa, mynum)
tm = time.clock() - tm 
print(' Время выполнения поиска Фибоначчи: ' + str(tm)+ '\n')


# In[89]:


with open('array200.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[21]
tm = time.clock()
res = LinearSearch(sa, mynum)
tm = time.clock() - tm 
print('\n Результаты для массива 200\n')
print('   Индекс: ' + str(res) + '\n')
print(' Время выполнения линейного поиска: ' + str(tm)+ '\n')

with open('array200.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[21]
tm = time.clock()
res1 = BinarySearch(sa, mynum)
tm = time.clock() - tm 
print(' Время выполнения бинарного поиска: ' + str(tm)+ '\n')


with open('array200.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[21]
tm = time.clock()
res1 = FibonacciSearch(sa, mynum)
tm = time.clock() - tm 
print(' Время выполнения поиска Фибоначчи: ' + str(tm)+ '\n')


# In[90]:


with open('array500.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[301]
tm = time.clock()
res = LinearSearch(sa, mynum)
tm = time.clock() - tm 
print('\n Результаты для массива 500\n')
print('   Индекс: ' + str(res) + '\n')
print(' Время выполнения линейного поиска: ' + str(tm)+ '\n')

with open('array500.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[301]
tm = time.clock()
res1 = BinarySearch(sa, mynum)
tm = time.clock() - tm 
print(' Время выполнения бинарного поиска: ' + str(tm)+ '\n')


with open('array500.txt', 'r') as af:
    sa = json.load(af)
mynum = sa[301]
tm = time.clock()
res1 = FibonacciSearch(sa, mynum)
tm = time.clock() - tm 
print(' Время выполнения поиска Фибоначчи: ' + str(tm)+ '\n')


# In[ ]:





# In[ ]:




