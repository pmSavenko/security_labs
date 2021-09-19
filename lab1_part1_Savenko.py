#!/usr/bin/env python
# coding: utf-8

# In[5]:


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


# In[6]:


def bubble_sort(ar):
    i = 0
    N = len(ar)
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
            j += 1
        i += 1
    print (ar)
    return (ar)

def shellSort(ar):
    N = len(ar)
    k = int(math.log(N)/math.log(2))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, N):
            temp = ar[i]
            j = i
            while j >= interval and ar[j - interval] > temp:
                ar[j] = ar[j - interval]
                j -= interval
            ar[j] = temp
        k -= 1
        interval = 2**k -1
    return ar

with open('array50.txt', 'r') as af:
    sa = json.load(af)
tm = time.clock()
sa = bubble_sort(sa)
tm = time.clock() - tm
    
print('\n Результаты для массива 50\n')
print(' Время выполнения пузырьковой сортировки: ' + str(tm))

with open('array50.txt', 'r') as af:
    sa = json.load(af)
tm = time.clock()
sa = shellSort(sa)
tm = time.clock() - tm

print(' Время выполнения сортировки Шелла: ' + str(tm))


# In[7]:


with open('array200.txt', 'r') as af:
    sa = json.load(af)
tm = time.clock()
sa = bubble_sort(sa)
tm = time.clock() - tm
    
print('\n Результаты для массива 200\n')
print(' Время выполнения пузырьковой сортировки: ' + str(tm))

with open('array200.txt', 'r') as af:
    sa = json.load(af)
tm = time.clock()
sa = shellSort(sa)
tm = time.clock() - tm

print(' Время выполнения сортировки Шелла: ' + str(tm))


# In[8]:


with open('array500.txt', 'r') as af:
    sa = json.load(af)
tm = time.clock()
sa = bubble_sort(sa)
tm = time.clock() - tm
    
print('\n Результаты для массива 500\n')
print(' Время выполнения пузырьковой сортировки: ' + str(tm))

with open('array500.txt', 'r') as af:
    sa = json.load(af)
tm = time.clock()
sa = shellSort(sa)
tm = time.clock() - tm

print(' Время выполнения сортировки Шелла: ' + str(tm))


# In[ ]:





# In[ ]:




